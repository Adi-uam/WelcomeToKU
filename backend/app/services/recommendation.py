from app.ml.predictor import predict_grant_probability
from app.services.groq_client import get_specialties_from_groq
SPECIALTIES = {
    "IT": ["math", "physics", "coding", "videogame", "programming"],
    "Medicine": ["biology", "animals" "chemistry"],
    "Business": ["economics", "money", "management"],
    "Law": ["history", "human rights", "law"],
}


def match_specialties(interests):
    result = []

    for spec, keywords in SPECIALTIES.items():
        score = len(set(interests) & set(keywords))
        if score > 0:
            result.append((spec, score))

    result.sort(key=lambda x: x[1], reverse=True)

    return [r[0] for r in result]


def get_recommendation(student):
    prob = predict_grant_probability(student.gpa, student.ent_score)
    groq_result = get_specialties_from_groq(student.interests)
    
    return {
        "recommended_specialties": groq_result["specialties"],
        "grant_probability": prob ,
        "explanation" : groq_result["explanation"]
    }