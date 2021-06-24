from flask import Flask
from flask import render_template
from flask import request as rq
import requests
import json

from requests.api import request

app = Flask(__name__)

AutoML_url = "https://portal-automl-ensaas.education.wise-paas.com/94e8d76a-cc81-4fc2-b4d3-f57b4018e075/YienTest/predict"

headers = {
  'Content-Type': 'application/json'
}



@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/', methods=['GET'])
def main():
    return "Hello Advantech!"

@app.route('/api', methods=['POST'])
def api_return():
    
    request_data=rq.get_json()

    kw_fan = request_data[0]['KW_FAN']
    status_fan = request_data[0]['STATUS_FAN']
    voltage_input = request_data[0]['VOLTAGE_INPUT']
    status_equipment = request_data[0]['STATUS_EQUIPMENT']

    payload = json.dumps([
        {
            "KW_FAN": kw_fan,
            "STATUS_FAN": status_fan,
            "VOLTAGE_INPUT": voltage_input,
            "STATUS_EQUIPMENT": status_equipment
        }
    ])

    response = requests.request("POST", AutoML_url, headers=headers, data=payload)
    output = json.dumps([{"Temperature_predict": str(eval(response.text)[0])}])
    return output

app.run(host="0.0.0.0", port=3000)