import requests
from datetime import datetime
import os
from config import SHEETY_PASS, SHEETY_URL

GENDER = "male"
WEIGHT = 58
HEIGHT = 167.64
AGE = 22

SHEETY_USER = "Gowthamvegi"
# SHEETY_PASS = os.environ['SHEETY_PASS']

API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": "2c7febf4",
    "x-app-key": "56c203119696c84221ca357165d83a75",
    "x-remote-user-id": "0"
}

exercise_text = input("Tell me which exercises you did: ")

params = {
     "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=API_ENDPOINT, json=params, headers=headers)
response.raise_for_status()
data = response.json()

current_datetime = datetime.now()

date = current_datetime.date().strftime("%d/%m/%y")
time = current_datetime.time().strftime('%H:%M:%S')


for exercise in data['exercises']:
    basic = (SHEETY_USER, SHEETY_PASS)
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_URL, json=sheet_inputs, auth=basic)
    # print(sheet_response.text)



