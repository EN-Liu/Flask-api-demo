import requests
import json

url = "https://portal-automl-ensaas.education.wise-paas.com/94e8d76a-cc81-4fc2-b4d3-f57b4018e075/YienTest/predict"

payload = json.dumps([
  {
    "KW_FAN": "2.5",
    "STATUS_FAN": "1",
    "VOLTAGE_INPUT": "215",
    "STATUS_EQUIPMENT": "0"
  }
])
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

output = json.dumps([{"TEMPERATURE_OUTPUT": str(eval(response.text)[0])}])
print(output)