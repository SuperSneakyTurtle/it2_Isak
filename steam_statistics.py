import json
import math

amount: int = 0
games_played: int = 0
current_highest = -math.inf

with open("games.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for i in range(0, len(data["spill"])):
    amount +=1
    if data["spill"][i]["playtime_forever"] > 0:
        games_played += 1
    
print(amount, games_played)

#check list
#antall spill: x
#Antall spill spilt: x
#top 5 høyest spilletid: 
