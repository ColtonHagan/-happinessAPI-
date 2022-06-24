from flask import Flask
from flask_restful import Api, Resource, abort
import os
import mysql.connector

app = Flask(__name__)
api = Api(app)

#
def databaseCall(sql):
    #TODO add error check to see if can connect to database using try
    connection = mysql.connector.connect(user='root', password='root', host='mysql', port='3306', database='db')
    cursor = connection.cursor()
    cursor.execute(sql)
    output = cursor.fetchall()
    connection.close()
    return output

#Get happiness indice by country id
class Happiness(Resource):
    def get(self, country_id):
        happiness = databaseCall("select HappinessIndex FROM happiness WHERE CountryId = " + str(country_id))
        if(not happiness): abort(400, error="Country id is not in database")
        return {"happiness": float(happiness[0][0])}
api.add_resource(Happiness,"/by_id/<int:country_id>")

#TODO Get average happiness of all countries in database 
class Average(Resource):
    def get(self):
        #Error check if it exists 
        #input check correct input
        mean = databaseCall("select Avg(HappinessIndex) FROM happiness")
        return {"Mean": float(mean[0][0])}
api.add_resource(Average,"/average")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)