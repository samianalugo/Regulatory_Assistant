from pydantic import BaseModel
from typing import List

class ReportRequest(BaseModel):
    report: str 

class ReportResponse(BaseModel):
    id: int 
    drug: str 
    adverse_events: List[str]
    severity: str 
    outcome: str 

class TranslateRequest(BaseModel):
    outcome: str 
    lang: str    