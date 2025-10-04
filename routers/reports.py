from fastapi import APIRouter, HTTPException
from models import ReportRequest, ReportResponse
from extractors import process_report_text
from crud import save_report, get_reports


router = APIRouter()

@router.post("/process-report", response_model=ReportResponse)
def process_report(req: ReportRequest):
    if not req.report.strip():
        raise HTTPException(status_code=400, detail="Report text is empty")

    extracted = process_report_text(req.report)
    record_id = save_report(req.report, extracted)
    return {**extracted, "id": record_id}

@router.get("/reports")
def fetch_reports():
    return get_reports()
