import requests
from datetime import datetime
import os

# for security purpose
APP_ID=os.environ.get('APP_ID')
APP_KEY=os.environ.get('APP_KEY')
SHEETY_ENDPOINT=os.environ.get('SHEETY_ENDPOINT')                  # save env veriable bt set SHEETY_ENDPOINT=httpsfkaf... and run  
SHEETY_AUTHENTICATION_CODE=os.environ.get('SHEETY_AUTHEN_CODE')

query=input('What you did today?')
nutritionix_excersice_nlp_endpoint='https://trackapi.nutritionix.com/v2/natural/exercise'
header={
    'x-app-id':APP_ID,
    'x-app-key':APP_KEY,
}
params={
 "query":query,
 "gender":"male",
 "weight_kg":60,
 "height_cm":175.64,
 "age":21
}

response=requests.post(url=nutritionix_excersice_nlp_endpoint,json=params,headers=header)
response.raise_for_status()
print(response.json())
results=response.json()


for result in results['exercises']:
    date_now=datetime.now()
    date=date_now.strftime("%d/%m/%Y")
    time=date_now.strftime('%H:%M:%S')
    sheety_endpoint=SHEETY_ENDPOINT
    data={
        'workout':{
            'date':date,
                "time": time,
                "exercise": result['name'],
                "duration": result['duration_min'],
                "calories": result['nf_calories']
        }
    }
   
    # basic authentication is enabled 
    header={
        "Authorization":f"Basic {SHEETY_AUTHENTICATION_CODE}",
    }
    response_sheety=requests.post(url=sheety_endpoint,json=data,headers=header)
    response_sheety.raise_for_status()
