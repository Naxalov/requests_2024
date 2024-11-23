import requests
 
r = requests.get('https://randomuser.me/api/')
# Print status code
print(r.status_code)
