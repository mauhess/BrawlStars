global response
def get_from_battle(i, value, response):
    return response["items"][i]["battle"][value]

def main(response, tag, i):
    battle_mode = get_from_battle(i, "mode", response)
    battle_type = get_from_battle(i, "type", response)
    battle_rank = str(get_from_battle(i, "rank", response))
    battle_map = response["items"][i]["event"]["map"]
    player = "__xx__"
    for j in range(10):
        if response["items"][i]["battle"]["players"][j]["tag"] == tag:
            player = response["items"][i]["battle"]["players"][j]
    champ_played = player["brawler"]["name"]
    trophies_start = str(player["brawler"]["trophies"])
    try:
        battle_trophy = str(get_from_battle(i, "trophyChange", response))
    except:  # no trophy change
        battle_trophy = "0"
    print(str(i + 1) + ": " + battle_mode + "_" + battle_type + ", map: " + battle_map + ", rank: " + battle_rank +
          ", Trophies: " + str(battle_trophy) + ", trophies started with: " + trophies_start +
          ", champion played: " + champ_played)

# WORKS