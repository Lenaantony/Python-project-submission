import requests
import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage
print(os.getcwd())
load_dotenv("api.env")


API_KEY=os.getenv("WEATHER_API_KEY")
EMAIL_ADDRESS=os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD=os.getenv("EMAIL_PASSWORD")
CITY="Thiruvananthapuram"

url=(
    f"https://api.openweathermap.org/data/2.5/forecast"
    f"?q={CITY}&appid={API_KEY}&units=metric"
)
response=requests.get(url)
data=response.json()

if "list" not in data:
    print("API Error:")
    print(data)
    exit()
temperature=data["list"][0]["main"]["temp"]
rain_predicted=False
for forecast in data["list"][:8]:
    if"rain" in forecast["weather"][0]["description"].lower():
        rain_predicted=True
        break
print("Temperature:", temperature)
print("Rain Predicted:", rain_predicted)

if temperature > 35 or rain_predicted:
    msg=EmailMessage()
    msg["Subject"] = "Weather Alert"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS
    msg.set_content(
        f"""
Temperature: {temperature}°C
Rain Predicted: {rain_predicted}

Weather alert triggered.
"""
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print("Alert email sent!")

else:
    print("Weather normal")