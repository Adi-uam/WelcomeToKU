from sqlalchemy import Column, Integer, Float, String
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    gpa = Column(Float)
    ent_score = Column(Integer)
    interests = Column(String)
    recommended = Column(String)
    grant_probability = Column(Float)