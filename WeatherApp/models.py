from dataclasses import dataclass

@dataclass
class Weather:
    city: str

    temperature: float
    
    feels_like: float

    humidity: int

    

    wind_speed: float

    visibility: int

    cloud_cover: int

    condition: str

    description: str
