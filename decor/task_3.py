import requests
import os
from task_2 import logger
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")


@logger("task_3.log")
def find_uk_city(coordinates, key):

    cities_list = ["Leeds", "London", "Liverpool", "Manchester",
                   "Oxford", "Edinburgh", "Norwich", "York"]
    for latitude, longitude in coordinates:
        url_base = "https://geocode.maps.co/reverse"
        params = {
            "lat": latitude,
            "lon": longitude,
            "api_key": key,
        }
        response = requests.get(url_base, params=params).json()
        city = response["address"]["city"]
        if city in cities_list:
            return city


coopdinates_city = [
    ('55.7514952', '37.618153095505875'),
    ('52.3727598', '4.8936041'),
    ('53.4071991', '-2.99168')
]

if __name__ == "__main__":
    find_uk_city(coopdinates_city, API_KEY)
