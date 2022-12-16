from twilio.rest import Client
import smtplib
from flight_data import FlightData
MY_EMAIL = "yeshacodes@gmail.com"
MY_PASSWORD = "yujjfkqvdfwdtnrr"
account_sid = "ACfc37337505347e37ea7a3c40fb822625"
auth_token = "ccf320eaf721926781a14fcbdd4020a7"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_message(self, flight):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"Low price alert! Only £{flight.price} to fly from {flight.departure_city_name}-"
                 f"{flight.departure_city_code} to {flight.arrival_city_name}-{flight.arrival_city_code},"
                 f" from {flight.inbound_date} to {flight.outbound_date}.",
            from_='+13465507115',
            to='+919979231095'
        )

        print(message.sid)

    def send_emails(self, flight,user_email):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=user_email,
                                msg=f"Low price alert! Only {flight.price} to fly from "
                 f"{flight.departure_city_code} to {flight.arrival_city_code},"
                 f" from {flight.inbound_date} to {flight.outbound_date}.\n Link is: {flight.link}")
