from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint
import flask

def api():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
    'slug':'bitcoin',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'f1f79629-b25b-4092-92e9-61886b7cf49f',
    }

    session = Session()
    session.headers.update(headers)


    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    btcprice = data['data']['1']['quote']['USD']['price']
    return int(btcprice)


dictionary ={
    "price": api(),
}
  
# Serializing json 
json_object = json.dumps(dictionary, indent = 4)
  
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

print('ok')