import requests
import json 

r = requests.get('https://randomuser.me/api/')
# Print status code
print(r.status_code)
# print text of response
text = r.text
# convert text to json
json_data = json.loads(text)

# Get full name
first_name = json_data['results'][0]['name']['first']
last_name = json_data['results'][0]['name']['last']

# Get full name
full_name = first_name + " " + last_name
print(full_name)
