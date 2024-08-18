import requests
from twilio.rest import Client


# {only for older version}
# from twilio.http.http_client import TwilioHttpClient
# import os


API_Endpoint= "https://api.openweathermap.org/data/2.5/forecast"
api_key ="6fa100a830359497394f191bd61c1a33"

account_sid=<Account_id>
auth_token=<Key>

weather_params={
    "lat":17.4065,
    "lon":78.4772,
    "appid":api_key,
    "cnt" : 4

}

response = requests.get(url = API_Endpoint , params = weather_params)
data = response.json()
#print(data["list"][0]["weather"][0])

will_rain = False
for hour_data in data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain=True

if will_rain:
    client = Client(account_sid, auth_token)

    #{only for older version
    #proxy_client = TwilioHttpClient()
    #proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    #client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages.create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_='+15017122661',
        to='+15558675310'
    )