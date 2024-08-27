import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "chuchugaming8@gmail.com"
PASSWORD = "obphqynffyohbbyo"

HEADERS = {
    "User-Agent":"Defined",
    "Accept-Language":"en-US,en;q=0.9"
}

url = "https://www.amazon.in/Boult-Audio-Lightning-Environmental-Cancellation/dp/B0B31BYXQQ/?_encoding=UTF8&pd_rd_i=B0B31BYXQQ&pd_rd_w=m6PAV&content-id=amzn1.sym.54266ae0-89ca-4e6d-8d7c-dd5a40ca3101&pf_rd_p=54266ae0-89ca-4e6d-8d7c-dd5a40ca3101&pf_rd_r=920R00SHFCW8CPP8NAV7&pd_rd_wg=zY6h7&pd_rd_r=7a32e11c-83ae-4c8b-af49-dbb665cf8f98&ref_=deals"

ROBOT_RESPONSE = "Sorry, we just need to make sure you're not a robot. For best results, please make sure your browser is accepting cookies."

buying_price = 750

robot_check = True
while robot_check == True:
    response = requests.get(url=url, headers=HEADERS)
    response.raise_for_status()
    web_page = response.text

    soup = BeautifulSoup(web_page, "html.parser")
    test = soup.find(name="p").text
    if test != ROBOT_RESPONSE:
        robot_check = False

price = soup.find(name="span", class_="a-price-whole").getText()
price = price.split(".")
price = (price[0])
price = int(price)
print (price)

if price <= buying_price :
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Price Drop \n\n There is price drop in the product you are tracking BuyNow:{url} ."
        )
