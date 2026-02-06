SPORT_COEFFICIENT = {
    "run": 1.0,
    "trail": 1.1,
    "bike": 0.7,
    "swim": 0.5,
    "ski": 0.9,
    "strength": 0.8,
}


def weighted_load(trimp, sport):
    return trimp * SPORT_COEFFICIENT.get(sport, 1.0)
