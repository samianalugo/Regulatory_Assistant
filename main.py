from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
import os
from database import init_db
from routers import reports, translate


app = FastAPI(title = "Mini- Regulatory-Report- Assistant")


# allows CORS (update origins for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#init database at startup
init_db()

#include routers
app.include_router(reports.router, prefix="", tags=["Reports"])
app.include_router(translate.router, prefix="", tags=["Translate"])

"""Serve React build if available, else return JSON health message."""

# Compute absolute paths so the runtime finds build files regardless of CWD
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(ROOT_DIR, "frontend", "build")
build_static_dir = os.path.join(build_dir, "static")
if os.path.isdir(build_static_dir):
    app.mount("/static", StaticFiles(directory=build_static_dir), name="static")


@app.get("/")
def root():
    index_path = os.path.join(build_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "Mini Regulatory Report Assistant API is running"}


@app.get("/__build_debug")
def build_debug():
    info = {"build_dir": os.path.abspath(build_dir)}
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