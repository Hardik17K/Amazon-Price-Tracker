from bs4 import BeautifulSoup
import requests
import smtplib

BUY_PRICE = 1500
EMAIL = "9810474178h@gmail.com"
PASSWORD = "hardik@1723"
URL = "https://www.amazon.in/Rockerz-510-Wireless-Bluetooth-Headphones/dp/B06Y5LK5QJ/ref=sr_1_1?crid=1GMKLY0TAGUES&keywords=boat+rockerz+510&qid=1642059947&sprefix=boat+rockerz+510%2Caps%2C244&sr=8-1"
headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0)"
                  " Gecko/20100101 Firefox/90.0"
}

response = requests.get(URL, headers=headers)
print(response)
site_data = response.text
soup = BeautifulSoup(site_data, "html.parser")
price_data = soup.find(name="span", class_="a-offscreen")
price_data_text = price_data.getText()

price_with_c = price_data_text.split("₹")[1].split(".")[0]
print(price_with_c)

if price_with_c.find(",") == 1:
    price1 = price_with_c.split(",")[0]
    price2 = price_with_c.split(",")[1]
    price = int(price1+price2)
else:
    price = int(price_with_c)
title = soup.find(id="productTitle").get_text().strip()
message = f"{title} is now Rs{price} {URL}"

if price < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}"
        )



