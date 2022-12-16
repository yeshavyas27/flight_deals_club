#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

data = DataManager()
city = FlightSearch()
messager = NotificationManager()
low_price_flight = FlightData()

sheet_data = data.get_sheet_data()
# Searching codes for city names
for row in sheet_data:
    if row["iataCode"] == "":
        city_name = str(row["city"])
        iata_code = city.search_code(city_name)
        print(iata_code)
        row["iataCode"] = iata_code
        data.add_data(row["id"], row["iataCode"])
user_data = data.get_user_data()
for row in sheet_data:
    city_code = row["iataCode"]
    response = city.flight_searching("LON", city_code)

    try:
        price = response.json()["data"][0]["price"]


        if price < row["lowestPrice"]:
            low_price_flight.price = price
            low_price_flight.arrival_city_name = response.json()["data"][0]["cityTo"]
            low_price_flight.arrival_city_code = response.json()["data"][0]["cityCodeTo"]
            low_price_flight.departure_city_name = response.json()["data"][0]["cityFrom"]
            low_price_flight.departure_city_code = response.json()["data"][0]["cityCodeFrom"]
            low_price_flight.inbound_date = response.json()["data"][0]["local_departure"][:10]
            low_price_flight.outbound_date = response.json()["data"][0]["local_arrival"][:10]
            low_price_flight.link = f"https://www.google.co.uk/flights?hl=en#flt={low_price_flight.departure_city_code}." \
            f"{low_price_flight.arrival_city_code}." \
            f"{low_price_flight.inbound_date}*{low_price_flight.arrival_city_code}." \
            f"{low_price_flight.departure_city_code}.{low_price_flight.outbound_date}"

            for user in user_data["users"]:
                messager.send_emails(low_price_flight, user["email"])


    except IndexError:
        print(f"No flights for {row['iataCode']}")
