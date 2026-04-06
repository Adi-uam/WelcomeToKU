import os 
import json
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SPECIALTIES =["IT", "Medicine", "Business" , "Law" , "Engineering" , "Education"]

def get_specialties_from_groq(interests : list[str]) -> dict :
    prompt = f"""
    У студента следующие интересы {",".join(interests)}
    доступные специальности : {",".join(SPECIALTIES)}
    верни только JSON массив подходящих специальностей в таком формате :
    {{
        "specialties" : ["IT" , "Engineering"],
        "explanation" : "Краткое описания почему эти специальности подходят"
    }}
    """
    responce = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = [{"role": "user", "content" : prompt}],
        temperature = 0.3,
        max_tokens = 100 # дофига экономный
    )
    text = responce.choices[0].message.content.strip()
    if "```" in text:
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text [4:]
    text = text.strip()
    try: 
        result = json.loads(text)
        return result
    except json.JSONDecodeError:
        return {"specialties" : [] , "explanation" : "Не удалось определить содержимое специальности"}
    # парсинг ответа