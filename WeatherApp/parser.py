from .models import Weather


def parse_weather(weather_data): #Takes Json file and Returns it as a readable Weather Object

    city = weather_data["name"]
    temperature = weather_data["main"]["temp"]
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data["main"]['humidity']
    wind_speed = weather_data["wind"]['speed']
    visibility = weather_data["visibility"]
    cloud_cover = weather_data["clouds"]["all"]
    condition = weather_data["weather"][0]["main"]
    description = weather_data["weather"][0]["description"]
    return Weather(
        city=city,
        temperature=temperature,
        feels_like=feels_like,
        humidity=humidity,
        wind_speed=wind_speed,
        visibility=visibility,
        cloud_cover=cloud_cover,
        condition=condition,
        description=description,
)