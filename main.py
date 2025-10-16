from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
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

@app.get("/")
def root():
    return {"message": "Mini Regulatory Report Assistant API is running"}