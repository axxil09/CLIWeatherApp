import os
import groq
from models import Weather
from groq import Groq
from dotenv import load_dotenv
from errors import LLMServiceError
load_dotenv()





def build_prompt(weather : Weather) -> str: #Build the prompt which we pass to groq to get the advice.
    
    return f"""
    You are an expert weather analyst.

Analyze the following weather report.

Rules:
- Respond with advice
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


def generate_advice(prompt: str) -> str: # Retrieve Advice from groq 
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    if not GROQ_API_KEY:
        raise LLMServiceError(
            "Groq API key not found. Please configure GROQ_API_KEY in your .env file."
        )
    client = Groq(api_key=GROQ_API_KEY)
    MODEL_NAME = "llama-3.1-8b-instant"
    MAX_TOKENS = 100
    TEMPERATURE = 0.7   
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE
        )
        return response.choices[0].message.content
    except groq.RateLimitError as e:
        raise LLMServiceError(f"Groq API rate limit exceeded. Please try again later.") from e
    except groq.AuthenticationError as e:
        raise LLMServiceError(f"Invalid Goq API key.") from e
    except groq.APIStatusError as e:
        raise LLMServiceError(f"Groq service returned status code {e.status_code}.") from e
    except groq.APIConnectionError as e:
        raise LLMServiceError(f"Unable to connect to the Groq service.") from e
    except groq.APIError as e:
        raise LLMServiceError(f"Unexpected Groq API error.") from e