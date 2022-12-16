import requests
import datetime
SEARCH_IATACODE_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
FLIGHT_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
API_KEY = "9jnmYJ3bYzD4gUWP_EQQJ1Uv1DqGfokm"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def search_code(self, city_name):
        header = {
            "apikey": API_KEY
        }
        parameters = {
            "term": city_name,
            "location_types": "city"

        }
        response = requests.get(url=SEARCH_IATACODE_ENDPOINT, headers=header, params=parameters)
        results = response.json()["locations"]
        iata_code = results[0]["code"]
        return iata_code

    def flight_searching(self, from_code, to_code):

        today = datetime.datetime.now().strftime("%d/%m/%Y")
        date = datetime.datetime.now() + datetime.timedelta(days=44)
        till_date = date.strftime("%d/%m/%Y")

        header = {
            "apikey": API_KEY
        }
        parameters = {
            "fly_from": from_code,
            "fly_to": to_code,
            "return_from": today,
            "return_to": till_date,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP"

        }

        response = requests.get(url=FLIGHT_SEARCH_ENDPOINT, headers=header, params=parameters)
        return response
