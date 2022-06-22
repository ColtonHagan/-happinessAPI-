#TEMP testing for primative version of api
import requests

BASE_URL = "http://127.0.0.1:5000/"

#Should work
response = requests.get(BASE_URL + "by_id/12345")
print(response.json())

#Should fail
response = requests.get(BASE_URL + "by_id/2")
print(response.json())