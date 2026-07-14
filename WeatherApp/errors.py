class WeatherError(Exception):
    pass
class WeatherAPIError(WeatherError):
    def __init__(self, status_code: int):
        self.status_code = status_code
        super().__init__(
            f"Weather API returned status code {status_code}."
        )

class CityNotFoundError(WeatherError):
    def __init__(self, city: str):
        self.city = city
        super().__init__(f"City '{city}' was not found.")
class WeatherAPIError(WeatherError):
    pass

class LLMServiceError(WeatherError):
    pass