from dataclasses import dataclass
from datetime import datetime


@dataclass
class TrainingSession:
    date: datetime
    sport: str
    duration_min: float
    avg_hr: float
    hr_max: float
    hr_rest: float
    distance_km: float = 0
    elevation_m: float = 0
