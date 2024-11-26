import requests
import json 




number_of_users = 10
users = []

while len(users) < number_of_users:
    r = requests.get('https://randomuser.me/api/')
    print(r.status_code)
    user = r.json()['results'][0]
    gender = user['gender']
    if gender == 'male':

        users.append(
            {
                'first_name': user['name']['first'],
                'last_name': user['name']['last'],
                'country': user['location']['country'],
                'city': user['location']['city'],
            }
        )

with open('users.json', 'w', encoding='utf-8') as f:
    json.dump(users, f, ensure_ascii=False, indent=4)

