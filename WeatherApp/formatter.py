from .models import Weather
def weather_to_text(weather: Weather) -> str: #Takes a Weather Object and Format it for better readability
    
    return (
    """       -------------------- 
       ||🌤  Weather Report ||
       --------------------\n"""
    
    f"📍 City         : {weather.city}\n"
    f"🌡 Temperature  : {weather.temperature:.1f} °C\n"
    f"🥵 Feels Like   : {weather.feels_like:.1f} °C\n"
    f"💧Humidity     : {weather.humidity}%\n"
    f"🌬 Wind Speed   : {weather.wind_speed} m/s\n"
    f"👁 Visibility   : {weather.visibility} m\n"
    f"☁  Cloud Cover  : {weather.cloud_cover}%\n"
    f"🌥 Condition    : {weather.condition}\n"
    f"📝 Description  : {weather.description.title()}\n"
)
def advice_to_text(advice : str) -> str: #Formats The Raw Text Groq 
    try:
        advice = advice.replace(". ", ".\n", 1)
    except Exception:
        return  
    return f"""
            Advice For The Day
        -----------------------------
{advice}
    """
