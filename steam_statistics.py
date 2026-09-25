import json
import math

amount: int = 0
games_played: int = 0
ordered_playtime: list = []
current_playtime: int = 0

with open("games.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for i in range(0, len(data["spill"])):
    amount +=1
    self_info: tuple = [data["spill"][i]["name"], data["spill"][i]["playtime_forever"]]
    if data["spill"][i]["playtime_forever"] > 0:
        games_played += 1


    for j in range(len(ordered_playtime)):
        print(ordered_playtime, data["spill"][i]["playtime_forever"])

        if len(ordered_playtime) == 0:
            ordered_playtime.insert(j, self_info)

        elif ordered_playtime[j][1] < data["spill"][i]["playtime_forever"]:
            ordered_playtime.insert(j, self_info)

    
print(amount, games_played)


#check list
#antall spill: x
#Antall spill spilt: x
#top 5 høyest spilletid: 
