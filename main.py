import os
import requests
import datetime as dt
APP_ID = os.environ.get('NUT_APP_ID')
API_KEY = os.environ.get('NUT_API_KEY')

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": query,
    "gender": 'male',
    "weight_kg": 94,
    "height_cm": 186,
    "age": 29
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

SHEETY_API_KEY = os.environ.get('SHEETY_API_KEY')
USER = os.environ.get('SHEETY_USER_NAME')
PASSWORD = os.environ.get('SHEETY_PASSWORD')
sheety_end_point = f'https://api.sheety.co/{SHEETY_API_KEY}/workoutTracking/workouts'


today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

for exercise in result['exercises']:
    exercise_name = exercise['name'].title()
    duration_of_ex = exercise['duration_min']
    calories_of_ex = exercise['nf_calories']
    body = {
        'workout':{
            'date':today_date,
            'time': now_time,
            'exercise':exercise_name,
            'duration':duration_of_ex,
            'calories':calories_of_ex
     }
    }

    my_sheety_req = requests.post(sheety_end_point, json=body, auth=(USER, PASSWORD))

    print(my_sheety_req.text)