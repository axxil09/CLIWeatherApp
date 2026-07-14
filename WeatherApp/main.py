from api import fetch_weather
from parser import parse_weather
from advisor import build_prompt, generate_advice
from formatter import weather_to_text, advice_to_text
from errors import WeatherError

def main():
    city = input("Enter Your City: ")
    try:
        raw_weather = fetch_weather(city)
    except WeatherError as e:
        print(f"❌ {e}")

    weather = parse_weather(raw_weather)
    print(weather_to_text(weather))
    prompt = build_prompt(weather)
    advice = generate_advice(prompt)
    print(advice_to_text(advice))
    
if "__main__" == __name__:
    main()
