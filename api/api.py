# Colton Hagan
# 6/26/23
# Create for EMSI for a Job Interview
# Purpose:
# API that manages database with countries fictional happeness index
# Allows users to get happiness_index of a given country 
# and statistics about the average for happiness_index
# Also allows users to put additional happiness_index data into database

from flask import Flask
from flask_restful import Api, Resource, abort, reqparse
import os
import mysql.connector

app = Flask(__name__)
api = Api(app)

#Parses args when putting new data
happiness_put_arg = reqparse.RequestParser()
happiness_put_arg.add_argument("happiness_index", type=float, help="Please include the happiness_index value", required=True)

#Creates server connection with database that has given information
def create_server_connection(username, password_name, host_name, port_name, db):
    connection = None
    try:
        connection = mysql.connector.connect(user=username,
            password=password_name,
            host=host_name,
            port=port_name, 
            database=db)
    except Error as err:
        abort(400, error=err)
    return connection

#Performs a safe sql call using given sql command
#if fetching is true returns fetched data, otherwise commits
def database_call(sql,var,fetching):
    output = None
    connection = create_server_connection("root", "root", "db", "3306", "db")
    cursor = connection.cursor()
    cursor.execute(sql,var)
    if(fetching): output = cursor.fetchall()
    else: connection.commit()
    connection.close()
    return output

#Get/posts happiness index by country id
class Happiness(Resource):
    def get(self, country_id):
        happiness = database_call("SELECT happiness_index FROM happiness WHERE country_id = %s", (country_id,), True)
        if(not happiness): abort(400, error="Country id is not in database")
        return {"Happiness index": float(happiness[0][0])}

    def put(self, country_id):
        if(database_call("SELECT happiness_index FROM happiness WHERE country_id = %s", (country_id,),True)):
            abort(400, error="Country id is already in database")
        happiness_index = happiness_put_arg.parse_args()["happiness_index"]

        #if entered value has more then one decimal place throws error
        if(len(str(happiness_index).split(".")[1]) > 1): 
            abort(400, error="Happiness_index should only have a number to one decimal place")

        database_call("INSERT INTO happiness (country_id, happiness_index) VALUES (%s, %s)", (country_id, happiness_index), False)
        return {"Sucesss": "added " + str(country_id)}

#Get average happiness and related statisics for happiness index of all countries in database
class Average(Resource):
    def get(self):
        mean = database_call("SELECT AVG(happiness_index) FROM happiness",(), True)
        mode = database_call("SELECT happiness_index FROM happiness GROUP BY happiness_index " +
                             "ORDER BY count(happiness_index) DESC LIMIT 1", (), True)
        maxHappy = database_call("SELECT MAX(happiness_index) FROM happiness", (), True)
        minHappy = database_call("SELECT MIN(happiness_index) FROM happiness", (), True)
        return {"Mean": round(float(mean[0][0]),1), 
                "Mode": round(float(mode[0][0]),1),
                "Max": round(float(maxHappy[0][0]),1),
                "Min": round(float(minHappy[0][0]),1),
                "Range": round(float((maxHappy[0][0] - minHappy[0][0])),1)
                }

api.add_resource(Happiness,"/happiness_by_country/<int:country_id>")
api.add_resource(Average,"/happiness_average")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)