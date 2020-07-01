import requests

url = "http://0.0.0.0:5000/api"

payload = "{\"t\":0.000172, \"CPU\":0.648571, \"RxKBTot\":0.000200, \"TxKBTot\":0.002441}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

