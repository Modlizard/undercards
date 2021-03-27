import json
with open('cards.json', 'r') as cardFile:
    cards = json.load(cardFile)
for x in cards:
    print(x)
