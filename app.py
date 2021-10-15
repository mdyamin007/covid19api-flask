from flask import Flask
import requests
from flask import request
from flask import jsonify
import ast
import json

app = Flask(__name__)

@app.route("/")
def index():
    data = requests.get("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.json").content
    str_data = data.decode('utf-8')
    dict_data = ast.literal_eval(str_data)
    new_data = []
    for _ in dict_data:
        new_data.append({
            "country": _['country'],
            "iso_code": _['iso_code'],
            "data": _['data'][-1]
        })
    return jsonify(new_data), 200