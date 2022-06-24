from flask import Flask
from flask_restful import Api, Resource, abort
import os
import mysql.connector

app = Flask(__name__)
api = Api(app)

#Error checks
#def abort_if_country_doesnt_exist(country_id):
    #if country_id not in db:
        #abort(404, error="Country id is not in database")
#def abort_if_country_exists(country_id):
    #if country_id in db:
        #abort(404, error="Country id already in database")

#Get happiness indice by country id
#class Happiness(Resource):
#    def get(self, country_id):
#        abort_if_country_doesnt_exist(country_id)
#        return {"happiness indice": db[country_id]}

#TODO Get average happiness of all countries in database 
#api.add_resource(Happiness,"/by_id/<int:country_id>")

##Testing sql database
class Test(Resource):
    def get(self):
        connection = mysql.connector.connect(user='root', password='root', host='mysql', port='3306', database='db')
        cursor = connection.cursor()
        cursor.execute('select FirstName FROM students')
        students = cursor.fetchall()
        connection.close()
        return {"student": students[0][0]}
api.add_resource(Test,"/")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)