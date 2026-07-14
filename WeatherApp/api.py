from dotenv import load_dotenv
from errors import CityNotFoundError, WeatherAPIError, LLMServiceError
import os
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city: str):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
    except requests.RequestException as e:
        raise WeatherAPIError("Unable To Connect To Weather Service") from e
    
    if response.status_code == 404:
        raise CityNotFoundError(city)

    if response.status_code != 200:
        raise WeatherAPIError(response.status_code) 


    return response.json()


