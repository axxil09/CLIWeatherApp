# 🌤 CLI Weather Advisor

An installable AI-powered command-line weather application built with Python.

CLI Weather Advisor retrieves real-time weather information from OpenWeatherMap and generates concise weather advice using Groq's Llama 3.1 model. The application features a clean terminal interface, animated loading screen, persistent configuration, and robust error handling.

---

## ✨ Features

- 🌍 Live weather information
- 🤖 AI-generated weather advice
- 🏃 Animated loading screen
- 🎨 Beautiful terminal output
- ⚙️ Persistent configuration
- ⚠️ Robust error handling
- 📦 Installable CLI application
- 🧩 Modular project architecture

---

## 📸 Sample Output

```text
$ weather

Enter Your City: Kochi

       🌤 Weather Report

📍 City         : Kochi
🌡 Temperature  : 25.5 °C
🥵 Feels Like   : 26.4 °C
💧 Humidity     : 88%
🌬 Wind Speed   : 1.34 m/s
👁 Visibility   : 10000 m
☁ Cloud Cover  : 90%
🌥 Condition    : Clouds
📝 Description  : Overcast Clouds

        💡 Advice For The Day

Wear light, breathable clothing due to high humidity.
Consider carrying an umbrella for cloudy conditions.
```

---

# 📂 Project Structure

```text
CLIWeather/
│
├── WeatherApp/
│   ├── __init__.py
│   ├── advisor.py
│   ├── api.py
│   ├── config.py
│   ├── errors.py
│   ├── formatter.py
│   ├── main.py
│   ├── models.py
│   ├── parser.py
│   └── ui.py
│
├── .env.example
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt
```

---

# 🛠 Built With

- Python 3
- OpenWeatherMap API
- Groq API
- Llama 3.1 8B Instant
- Requests
- python-dotenv

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/axxil09/CLIWeatherApp.git
cd CLIWeatherApp
```

Install the application:

```bash
pip install .
```

For development:

```bash
pip install -e .
```

You can also install globally using **pipx**:

```bash
pipx install .
```

---

# ⚙️ Initial Configuration

Before using the application, configure your API keys.

Run:

```bash
weather config
```

You'll be prompted for:

```text
OpenWeatherMap API Key:
Groq API Key:
```

The configuration is stored locally on your machine and only needs to be completed once.

---

# ▶️ Usage

After configuration:

```bash
weather
```

Enter a city name and receive:

- Live weather report
- AI-generated weather advice

---

# ⚠️ Error Handling

The application gracefully handles:

- Invalid city names
- Missing configuration
- Invalid API keys
- Network failures
- API rate limits
- Weather service errors
- Groq API errors
- Keyboard interruption (`Ctrl+C`)

---

# 🧩 Architecture

| Module | Responsibility |
|---------|----------------|
| `main.py` | Application entry point |
| `api.py` | OpenWeatherMap integration |
| `advisor.py` | Groq AI integration |
| `parser.py` | Converts API response into Weather objects |
| `formatter.py` | Terminal output formatting |
| `config.py` | Configuration management |
| `ui.py` | Loading animation |
| `errors.py` | Custom exception hierarchy |
| `models.py` | Weather dataclass |

---

# 📈 Future Improvements

- Five-day forecast
- Temperature unit selection (°C / °F)
- Colored terminal themes
- Automatic location detection
- Weather history
- PyPI publishing

---

# 👨‍💻 Author

**Akhilesh P S**

GitHub: https://github.com/axxil09

---

# 📄 License

Licensed under the MIT License.