from flask import Flask
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app)

#TEMP dictiorary --replace with sql database
db = {
    12345: 102.7,
    10023: 99.3,
    19634: 100.0
    }
#Error checks
def abort_if_country_doesnt_exist(country_id):
    if country_id not in db:
        abort(404, error="Country id is not in database")

#Get happiness indice by country id
class Happiness(Resource):
    def get(self, country_id):
        abort_if_country_doesnt_exist(country_id)
        return {"happiness indice": db[country_id]}

#TODO Get average happiness of all countries in database 

api.add_resource(Happiness,"/by_id/<int:country_id>")

#Devolper mode replace with actual before release
if __name__ == "__main__":
    app.run(debug=True)