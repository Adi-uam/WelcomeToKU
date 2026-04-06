from pydantic import BaseModel
from typing import List

class StudentCreate(BaseModel):
    gpa: float
    ent_score: int
    interests: List[str]


class StudentResponse(BaseModel):
    recommended_specialties: List[str]
    grant_probability: float
    explanation : str