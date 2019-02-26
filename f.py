import requests
import re
from bs4 import BeautifulSoup
import json
from ratelimit import limits

@limits(calls=60, period=60)
def call_api(p):
    response = requests.get("https://osu.ppy.sh/api/get_match", params=p)
    if response.status_code != 200:
        raise Exception('API response: {}'.format(response.status_code))
    return json.loads(response.content)

def findPlayer(key, start, players):
    parameters = {"k": key, "mp": start}
    allGames = call_api(parameters)["games"]

    for games in allGames:
        for scores in games["scores"]:
            user_id = int(scores["user_id"])
            for player in players:
                if user_id == player:
                    return start
    return "Not Found"

def mainLoop(key, start, players):
    tempCount = 0
    count = 0
    while True:
        count += 1
        tempCount += 1
        result = findPlayer(key, start, players)
        if type(result) is int:
            print(f'Found a match! Link: https://osu.ppy.sh/community/matches/{result}. Total counted so far: {count}.')
            tempCount = 0
        start = start - 1
        if tempCount != 0 and tempCount % 500 == 0:
            print(f'No results found in last 500 links. Total counted so far: {count}.')
            tempCount = 0

key = input("API Key? ")
start = input("MP Link ID to start search from? ")
players = []
counter = 0
while True:
    counter += 1
    player_id = input(f'Player {counter} user ID? ')
    if not player_id and counter == 1:
        print("You must put at least one player's ID!")
    elif not player_id:
        break
    players.append(player_id)

mainLoop(key, start, players)
