import requests
import json 


API_KEY = 'a45a594e67814c30883787b95fec5af1'
base_url = 'https://randommer.io/api/Phone/Countries'
headers = {
    'X-Api-Key': API_KEY
}

response = requests.get(base_url, headers=headers)
data = response.json()

print(data)