# 🌤 CLI Weather Advisor

An AI-powered command-line weather application built with Python.

CLI Weather Advisor fetches real-time weather information from the OpenWeatherMap API and uses Groq's Llama 3.1 model to generate concise, practical weather advice. The application features a clean terminal interface, animated loading screen, and robust error handling.

---

## ✨ Features

- 🌍 Real-time weather information
- 🤖 AI-generated weather advice
- 🏃 Animated terminal loading screen
- 🎨 Clean and formatted CLI output
- ⚠️ Comprehensive error handling
- 🔒 Environment variable support using `.env`
- 🧩 Modular project architecture

---

## 📸 Sample Output

```text
Enter Your City: Kochi

       🌤 Weather Report

📍 City         : Kochi
🌡 Temperature  : 26.4 °C
🥵 Feels Like   : 26.4 °C
💧 Humidity     : 89%
🌬 Wind Speed   : 3.36 m/s
👁 Visibility   : 10000 m
☁ Cloud Cover  : 100%
🌥 Condition    : Clouds
📝 Description  : Overcast Clouds

💡 Advice For The Day

Wear light, breathable clothing to stay comfortable.
Stay hydrated throughout the day.
```

---

## 📂 Project Structure

```text
CLIWeather/
│
├── WeatherApp/
│   ├── __init__.py
│   ├── .env.example
│   ├── advisor.py
│   ├── api.py
│   ├── errors.py
│   ├── formatter.py
│   ├── main.py
│   ├── models.py
│   ├── parser.py
│   └── ui.py
│
├── .env
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt
```

---

## 🛠 Built With

- Python 3
- OpenWeatherMap API
- Groq API
- Llama 3.1 8B Instant
- Requests
- Python Dotenv

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/DebugWAkhil/CLIWeather.git
cd CLIWeather
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```powershell
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

Copy the example environment file:

```bash
cp WeatherApp/.env.example .env
```

Update it with your own API keys:

```env
API_KEY=your_openweathermap_api_key
GROQ_API_KEY=your_groq_api_key
```

Get your API keys from:

- OpenWeatherMap — https://openweathermap.org/api
- Groq Console — https://console.groq.com/keys

---

## ▶️ Running the Application

Run directly:

```bash
python WeatherApp/main.py
```

Or, if installed as a package:

```bash
weather
```

---

## ⚠️ Error Handling

The application gracefully handles:

- Invalid city names
- Missing API keys
- Network connectivity issues
- API authentication failures
- API rate limits
- Unexpected API errors
- Keyboard interruption (`Ctrl + C`)

---

## 💡 Architecture

The project follows a modular design.

| Module | Responsibility |
|---------|----------------|
| `api.py` | Fetch weather data from OpenWeatherMap |
| `advisor.py` | Generate AI weather advice using Groq |
| `parser.py` | Convert API response into a Weather model |
| `formatter.py` | Format weather report and advice for the terminal |
| `ui.py` | Terminal animation utilities |
| `errors.py` | Custom exception hierarchy |
| `models.py` | Weather dataclass |
| `main.py` | Application entry point |

---

## 📈 Future Improvements

- Five-day weather forecast
- Temperature unit selection (°C / °F)
- Colored terminal output
- Automatic location detection
- Weather history
- Packaged CLI installation via PyPI

---

## 👨‍💻 Author

**Akhilesh P S**

GitHub: https://github.com/DebugWAkhil

---

## 📜 License

This project is licensed under the MIT License.