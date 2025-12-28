import requests

def get_current_time(city: str) -> str:
    base_url = "http://worldtimeapi.org/api/timezone"
    zones = requests.get(base_url).json()

    for zone in zones:
        if city.lower() in zone.lower():
            data = requests.get(f"{base_url}/{zone}").json()
            return f"The current time in {city} is {data['datetime']}"

    return "Sorry, city not found."
