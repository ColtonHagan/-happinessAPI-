#Examples of API working
import requests

BASE_URL = "http://127.0.0.1:5000/"

response = requests.get(BASE_URL + "by_id/1")
print(response.json())

response = requests.put(BASE_URL + "by_id/1", {"happiness_index": 1.0})
print(response.json())

response = requests.get(BASE_URL + "by_id/1")
print(response.json())

#Testing api
#response = requests.get(BASE_URL)
#print(response.json())

#Should work
#response = requests.get(BASE_URL + "by_id/12345")
#print(response.json())

#Should fail
#response = requests.get(BASE_URL + "by_id/2")
#print(response.json())

