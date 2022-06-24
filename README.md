# Happiness API

## How to run locally

IMPORTANT- You will need docker for this to work. Download [here]([https://link-url-here.org](https://www.docker.com/)) if you do not have it.
1. Navigate to the file containing this project
2. Open the command prompt and enter
```
docker-compose build
docker-compose up
```
3. Wait for this to finish, it may take a while

You will know it has finished when you see this, and nothing new is appearing on the command prompt
```
/usr/sbin/mysqld: ready for connections. Version: '8.0.29'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL.
```
4. API should now be working try a get or pull request (described below)

## Getting information from the API

There are two GETS for this project 

1. http://127.0.0.1:5000/happiness_average

Which will return a JSON containing information about the average happiness index for all countries
```
{
    "Mean": 100,
    "Mode": 96.4,
    "Max": 105,
    "Min": 95,
    "Range": 10
}
```
2. http://127.0.0.1:5000/happiness_by_country/<country_id\>

Which will return a JSON containing the happiness index for the given <country_id\>
```
{
    "Happiness index": 98.2
}
```

## Updating the database

There are two ways to update the database

1. Enter the happiness.sql file and manually add/remove an insert sql command

2. Utilizing the API call a put request on "happiness_by_country/<country_id\>" and include it with a JSON containing a happiness_index

Example python code:

```
import requests
BASE_URL = "http://127.0.0.1:5000/"
requests.put(BASE_URL + "happiness_by_country/99999", {"happiness_index": 1})
```

## Example
Examples of code for all get and pull requests are in example.py


