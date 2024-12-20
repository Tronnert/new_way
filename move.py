import requests
import json
import os

token = os.getenv("NEW_WAY_TOKEN")
server_url = 'https://games-test.datsteam.dev/play/snake3d'
api = '/player/move'
url = f"{server_url}{api}"
headers = {
    'X-Auth-Token': token,
    'Content-Type': 'application/json'
}

with open("post.json") as file:
    data = json.load(file)

def move(directions):
    for e in range(3):
        data["snakes"][e]["direction"] = directions[e]
    response = requests.post(url, headers=headers, json=data)
    with open('example_response.json', 'w') as file:
        file.write(response.text)
    response = response.json()
    return (response["errors"], response["fences"], response["snakes"], 
    response["snakes"], response["enemies"], response["food"], 
    response["specialFood"], response["tickRemainMs"])



if __name__ == "__main__":
    print(move([[1, 0, 0], [1, 0, 0], [1, 0, 0]]), sep="\n\n\n")