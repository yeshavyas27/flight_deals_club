# This class is responsible for talking to the Google Sheet.

import requests
GET_ENDPOINT = "https://api.sheety.co/0124e3c397cd0ed21fa49c1eeb9c3f28/flightDeals/prices"
get_user_endpoint = "https://api.sheety.co/0124e3c397cd0ed21fa49c1eeb9c3f28/flightDeals/users"


class DataManager:
    def __init__(self):
        self.cities = []
        self.id = ""
        self.cities_IATA = []

    def get_sheet_data(self):
        response = requests.get(url=GET_ENDPOINT)
        return response.json()["prices"]

    def add_data(self, id, city_code):
        PUT_ENDPOINT = f"https://api.sheety.co/0124e3c397cd0ed21fa49c1eeb9c3f28/flightDeals/prices/{id}"
        body = {
            "price": {
                "iataCode": city_code
            }
        }
        response = requests.put(url=PUT_ENDPOINT, json=body)

    def get_user_data(self):
        response = requests.get(url=get_user_endpoint)
        return response.json()

