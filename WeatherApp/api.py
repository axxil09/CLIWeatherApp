from dotenv import load_dotenv
from errors import CityNotFoundError, WeatherAPIError
import os
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city: str) -> Weather: #Retrieve a json file carrying info related to the weather
    if not API_KEY:
        raise WeatherAPIError(
            "OpenWeatherMap API key not found. Please configure API_KEY in your .env file."
        )
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
    except requests.Timeout as e:
        raise WeatherAPIError(
        "The weather service took too long to respond.") from e

    except requests.RequestException as e:
        raise WeatherAPIError("Unable to connect to the weather service.")
        
    status = response.status_code
    
    if status == 401:
        raise WeatherAPIError("Invalid OpenWeatherMap API key.")

    if status == 404:
        raise CityNotFoundError(city)

    if status == 429:
        raise WeatherAPIError("Weather API rate limit exceeded.")

    if status != 200:
        raise WeatherAPIError(
        f"Weather service returned status code {response.status_code}."
        )


    return response.json()


