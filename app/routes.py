from flask import request
from app import app
from functions import getBrazilianStates, getBrazilianCities

@app.route('/states', methods=['GET'])
def getStates():
    where = request.get_json() if request.is_json else {}
    return getBrazilianStates.exec(where)

@app.route('/cities', methods=['GET'])
def getCities():
    where = request.get_json() if request.is_json else {}
    return getBrazilianCities.exec(where)


