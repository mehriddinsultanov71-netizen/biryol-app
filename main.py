from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import engine, get_db
from services import rag_service

# FastAPI obyektini ENG TEPAGA o'tkazamiz
app = FastAPI(title="WayUz Transport Ecosystem")

models.Base.metadata.create_all(bind=engine)

@app.post("/appeal/")
def create_appeal(appeal: schemas.AppealCreate, db: Session = Depends(get_db)):
    try:
        answer = rag_service.get_ai_answer(appeal.matn, appeal.yo_nalish)
        return {"status": "success", "answer": answer}
    except Exception as e:
        # Xatolikni terminalda ko'rsatish va brauzerga aniq sababini yuborish uchun
        print(f"Xatolik yuz berdi: {e}")
        return {"status": "error", "answer": f"Sun'iy intellekt xizmatida xatolik: {str(e)}"}