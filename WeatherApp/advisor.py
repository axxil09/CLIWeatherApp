import os
from models import Weather
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))




def build_prompt(weather : Weather) -> str:
    
    return f"""
    You are an expert weather analyst.

Analyze the following weather report.

Rules:
- Respond in exactly two short sentences.
- Each sentence must be under 12 words.
- Keep the total response under 30 words.
- Do not mention the city name.
- Do not repeat the weather report.
Weather Report:



    city : {weather.city}
    temperature : {weather.temperature}
    feels_like : {weather.feels_like}
    humidity : {weather.humidity}
    wind_speed : {weather.wind_speed}
    visibility : {weather.visibility}
    cloud_cover : {weather.cloud_cover}
    condition : {weather.condition}
    description : {weather.description}


"""


def generate_advice(prompt: str) -> str:   # ✅ accepts string directly
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"