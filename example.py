#Examples of API working
import requests

BASE_URL = "http://127.0.0.1:5000/"

#Starting average
print(requests.get(BASE_URL + "happiness_average").json())

#Getting 8059 happiness index
print(requests.get(BASE_URL + "happiness_by_country/8059").json())

#Attempting to get non-existant 99999 - SHOULD ERROR
print(requests.get(BASE_URL + "happiness_by_country/99999").json())

#Attemping to put already existing 8059 - SHOULD ERROR
print(requests.put(BASE_URL + "happiness_by_country/8059", {"happiness_index": 1.0}).json())

#Attemping to put invalid happiness_index - SHOULD ERROR
print(requests.put(BASE_URL + "happiness_by_country/99999", {"happiness_index": 1.5555}).json())

#Putting new entry for 99999
print(requests.put(BASE_URL + "happiness_by_country/99999", {"happiness_index": 1}).json())

#Showing new entry at 99999 exists
print(requests.get(BASE_URL + "happiness_by_country/99999").json())
print(requests.get(BASE_URL + "happiness_average").json())