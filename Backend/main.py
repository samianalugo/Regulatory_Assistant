from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from starlette.requests import Request
import os
import sys

# Ensure repository root is on sys.path so imports work whether
# the process is started from the `Backend/` directory or the repo root.
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(ROOT_DIR, ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

# import helpers/routers in a way that works whether this module is imported
# as a top-level module (uvicorn run from Backend/) or as a package
# database.py lives inside the Backend package so prefer a relative import
try:
    # When imported as a package (Backend.main)
    from .database import init_db
except Exception:
    # When run as a top-level module (uvicorn run from Backend/)
    from database import init_db

app = FastAPI(title="Mini- Regulatory-Report- Assistant")


# allows CORS (update origins for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# initialize database on FastAPI startup to avoid raising during module import
@app.on_event("startup")
def on_startup():
    init_db()

# include routers - import after app creation to avoid circular imports
def include_routers():
    from routers import reports, translate
    app.include_router(reports.router, prefix="", tags=["Reports"])
    app.include_router(translate.router, prefix="", tags=["Translate"])

# Call the function to include routers
include_routers()

"""Resolve CRA build directory for deployments where backend runs from Backend/.

Search order (first existing wins):
1) BUILD_DIR env var
2) <repo_root>/frontend/build (Backend/..../frontend/build)
3) <repo_root>/build (if service root already is frontend)
"""

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

candidate_build_dirs = []

env_build = os.getenv("BUILD_DIR")
if env_build:
    candidate_build_dirs.append(env_build)

# from Backend/ to repo root
candidate_build_dirs.append(os.path.normpath(os.path.join(ROOT_DIR, "..", "frontend", "build")))
candidate_build_dirs.append(os.path.normpath(os.path.join(ROOT_DIR, "..", "build")))

build_dir = next((p for p in candidate_build_dirs if os.path.isdir(p)), candidate_build_dirs[0])

build_static = os.path.join(build_dir, "static")
if os.path.isdir(build_static):
    app.mount("/static", StaticFiles(directory=build_static), name="static")


@app.get("/")
def root():
    index_path = os.path.join(build_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "Mini Regulatory Report Assistant API is running 🚀"}


# (SPA fallback moved to end of file so specific routes are matched first)


# Serve common root-level static files produced by Create React App
@app.get("/favicon.ico")
def favicon():
    fav = os.path.join(build_dir, "favicon.ico")
    if os.path.exists(fav):
        return FileResponse(fav)
    return {"detail": "Not Found"}


@app.get("/manifest.json")
def manifest():
    m = os.path.join(build_dir, "manifest.json")
    if os.path.exists(m):
        return FileResponse(m)
    return {"detail": "Not Found"}


@app.get("/asset-manifest.json")
def asset_manifest():
    am = os.path.join(build_dir, "asset-manifest.json")
    if os.path.exists(am):
        return FileResponse(am)
    return {"detail": "Not Found"}


@app.get("/robots.txt")
def robots():
    r = os.path.join(build_dir, "robots.txt")
    if os.path.exists(r):
        return FileResponse(r)
    return {"detail": "Not Found"}


# Debug endpoint used on Render to confirm build output exists
@app.get("/__build_debug")
def build_debug():
    info = {"build_dir": build_dir}
    index_path = os.path.join(build_dir, "index.html")
    info["index_exists"] = os.path.exists(index_path)
    files = []
    if os.path.isdir(build_dir):
        try:
            for entry in os.listdir(build_dir)[:50]:
                files.append(entry)
        except Exception as e:
            files.append(f"listing_error: {e}")
    info["entries_sample"] = files
    return info


# SPA fallback: serve React index.html for unknown non-API routes
@app.get("/{full_path:path}")
def spa_fallback(full_path: str, request: Request):
    if full_path.startswith("api/") or full_path in {"docs", "redoc", "openapi.json"}:
        return {"detail": "Not Found"}

    index_path = os.path.join(build_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "Mini Regulatory Report Assistant API is running 🚀"}
