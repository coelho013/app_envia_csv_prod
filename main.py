import requests
import json
import csv

url = ''
url_save = ''



payload = {}
headers = {
    'Appkey': '',
    'Token': '',
    'Username': '',
    'Password': ''
}

response = requests.request("POST", url + 'login', headers=headers, data=payload)

bearerToken = response.json().get('bearerToken')


def post_request(payload):
    headers_save = {
        'Content-Type': 'application/json',
        'Authorization' : 'Bearer '+ bearerToken
    }
    
    headers.update(headers_save)

    response = requests.request("POST", url + url_save, headers=headers, data=payload)
    return print(response.text)


with open('sqlcsv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='"')
    next(spamreader, None)

    for row in spamreader:
        newRow = row[0]

        payload = json.dumps({
        "serviceName": "",
        "requestBody": {
            "dataSetID": "",
            "entityName": "",
            "fields": [
            "CODPROD"
            ],
            "records": [
            {
                "values": {
                "0": newRow
                }
            }
            ]
        }
        })
        post_request(payload)
        

