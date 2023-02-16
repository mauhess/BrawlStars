global response
import googlesheet


def get_from_battle(value, response):
    return response["battle"][value]


def main(response, player, battle_time):
    battle_id = response["event"]["id"]
    battle_mode = get_from_battle("mode", response)
    battle_type = get_from_battle("type", response)
    battle_rank = str(get_from_battle("rank", response))
    battle_map = response["event"]["map"]
    player_battle_infos = "__xx__"
    for j in range(10):
        if response["battle"]["players"][j]["tag"] == player[0]:
            player_battle_infos = response["battle"]["players"][j]
    champ_played = player_battle_infos["brawler"]["name"]
    trophies_start = str(player_battle_infos["brawler"]["trophies"])
    try:
        battle_trophy = str(get_from_battle("trophyChange", response))
    except:  # no trophy change
        battle_trophy = "0"
    data = [[battle_time, battle_id, battle_mode, battle_type, battle_map, battle_rank, champ_played, trophies_start,
             battle_trophy]]
    googlesheet.add_data(player, data)
