from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from dotenv import load_dotenv
load_dotenv()

from app import models
from app.database import engine, get_db
from app.schemas import StudentCreate, StudentResponse
from app.services.recommendation import get_recommendation

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Welcome to KU AI Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AI Assistant is running"}


@app.post("/predict", response_model=StudentResponse)
def predict(student: StudentCreate, db: Session = Depends(get_db)):
    result = get_recommendation(student)

    db_student = models.Student(
        gpa=student.gpa,
        ent_score=student.ent_score,
        interests=",".join(student.interests),
        recommended=",".join(result["recommended_specialties"]),
        grant_probability=result["grant_probability"]
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return result