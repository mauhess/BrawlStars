global i, response

def get_from_battle(i, value, response):
    return response["items"][i]["battle"][value]
def get(i,response):
    return get_from_battle(i, "mode", response), get_from_battle(i, "type", response), response["items"][i]["event"]["map"]
def soloShowdown(i, tag, response):
    battle_mode, battle_type, battle_map = get(i, response)
    battle_rank = get_from_battle(i, "rank", response)
    player = "x"
    print(8)
    for j in range(10):
        if response["items"][i]["battle"]["players"][j]["tag"] == tag:
            player = response["items"][i]["battle"]["players"][j]
    champ_played = player["brawler"]["name"]
    trophies_start = str(player["brawler"]["trophies"])
    try:
        battle_trophy = str(get_from_battle(i, "trophyChange"))
    except:  # no trophy change
        battle_trophy = "0"
    print(battle_mode + "_" + battle_type + ", map: " + battle_map + ", rank: " + battle_rank + ", Trophies: " + str(
            battle_trophy) + ", trophies started with: " + trophies_start + ", champion played: " + champ_played)



def duoShowdown(i, tag):
    battle_mode, battle_type, battle_map = get(i)



def three_vs_three(i, tag):
    battle_mode, battle_type, battle_map = get(i)
