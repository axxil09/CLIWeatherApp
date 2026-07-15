from api import fetch_weather
from parser import parse_weather
from advisor import build_prompt, generate_advice
from formatter import weather_to_text, advice_to_text
from errors import WeatherError
from ui import start_animation, stop
def main():
    while True:
        
        city = input("Enter Your City: ")
        if not city.strip():
            print("Enter a Valid City")
            continue
        break
    animation = start_animation()
    try:
        raw_weather = fetch_weather(city)
        weather = parse_weather(raw_weather)
        prompt = build_prompt(weather)
        advice = generate_advice(prompt)
    
        
    except WeatherError as e:
        print(f"❌ {e}")
        return
    finally:
        stop()
        animation.join()
        print("\r" + " " * 60 + "\r", end="", flush=True)
    print(weather_to_text(weather))
    print(advice_to_text(advice))
    
if "__main__" == __name__:
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    