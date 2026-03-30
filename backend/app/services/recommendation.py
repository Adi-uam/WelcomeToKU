from app.ml.predictor import predict_grant_probability

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
    specialties = match_specialties(student.interests)

    return {
        "recommended_specialties": specialties,
        "grant_probability": prob
    }