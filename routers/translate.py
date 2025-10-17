# backend/routers/translate.py
from fastapi import APIRouter, HTTPException
# Translate router only needs the request model from Backend
from Backend.models import TranslateRequest

router = APIRouter()

TRANSLATIONS = {
    "fr": {
        "recovered": "rétabli",
        "ongoing": "en cours",
        "fatal": "mortel",
        "unknown": "inconnu"
    },
    "sw": {
        "recovered": "amepona",
        "ongoing": "inaendelea",
        "fatal": "kifo",
        "unknown": "haijulikani"
    }
}

@router.post("/translate")
def translate_outcome(req: TranslateRequest):
    lang = req.lang.lower()
    outcome = req.outcome.lower()

    if lang not in TRANSLATIONS:
        raise HTTPException(status_code=400, detail="Unsupported language")

    translated = TRANSLATIONS[lang].get(outcome, TRANSLATIONS[lang]["unknown"])
    return {"original": outcome, "lang": lang, "translated": translated}
