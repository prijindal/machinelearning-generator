import requests
import json
body = {
    "method": "neuralnetwork",
    "type": "regression",
    "kernel": "linear",
    "inputs": 2,
    "outputs": 2
}
body = json.dumps(body)
resp = requests.post("https://5xpj1pu5y8.execute-api.ap-south-1.amazonaws.com/dev/generator", data=body)
body = resp.json()
print(body)
# print(body["input"]["body"])
# print(body["code"])

with open('output.py', 'w+') as fl:
    fl.write(body["code"])
    fl.close()

import output
output.main()
