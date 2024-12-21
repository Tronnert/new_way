import requests
import json
import os
import datetime

token = os.getenv("NEW_WAY_TOKEN")
server_url = 'https://games-test.datsteam.dev/play/snake3d'
api = '/player/move'
url = f"{server_url}{api}"
headers = {
    'X-Auth-Token': token,
    'Content-Type': 'application/json'
}
session = requests.Session(verify=True)

with open("post.json") as file:
    data = json.load(file)

def move(directions, snake_ids):
    for e in range(3):
        data["snakes"][e]["direction"] = directions[e]
        data["snakes"][e]["id"] = snake_ids[e]
    
    response = session.post(url, headers=headers, json=data)
    # with open(f'responses/example_response_{datetime.datetime.utcnow().timestamp()}.json', 'w') as file:
    with open(f'responses/example_response_{"empty"}.json', 'w') as file: # datetime.datetime.utcnow().timestamp()
        file.write(response.text)
    response = response.json()
    # print(response)
    return (response["turn"], response["points"], response["errors"], response["fences"], response["snakes"], 
     response["enemies"], response["food"], 
    response["specialFood"], response["tickRemainMs"])



if __name__ == "__main__":
    print(move([[1, 0, 0], [1, 0, 0], [1, 0, 0]]), sep="\n\n\n")