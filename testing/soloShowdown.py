global response
import testing.googlesheet
from datetime import datetime


def get_from_battle(i, value, response):
    return response["items"][i]["battle"][value]

def main(response, player, i):
    battle_time = response["items"][i]["battleTime"]
    battle_time = battle_time[0:4] + "-" + battle_time[4:6] + "-" + battle_time[6:8] + " " + battle_time[9:11] + ":" + battle_time[11:13] + ":" + battle_time[13:]
    timestamps = testing.googlesheet.get_timestamps(player) # gets all timestamps of stored battles
    bt = str(battle_time)
    bt = [bt]
    if not(bt in timestamps): # checks if battle is already in excel file
        battle_id = response["items"][i]["event"]["id"]
        battle_mode = get_from_battle(i, "mode", response)
        battle_type = get_from_battle(i, "type", response)
        battle_rank = str(get_from_battle(i, "rank", response))
        battle_map = response["items"][i]["event"]["map"]
        player_battle_infos = "__xx__"
        for j in range(10):
            if response["items"][i]["battle"]["players"][j]["tag"] == player[0]:
                player_battle_infos = response["items"][i]["battle"]["players"][j]
        champ_played = player_battle_infos["brawler"]["name"]
        trophies_start = str(player_battle_infos["brawler"]["trophies"])
        try:
            battle_trophy = str(get_from_battle(i, "trophyChange", response))
        except:  # no trophy change
            battle_trophy = "0"
        data = [[battle_time, battle_id, battle_mode, battle_type, battle_map, battle_rank, champ_played, trophies_start, battle_trophy]]
        """print(str(i + 1) + ": " + battle_mode + "_" + battle_type + ", map: " + battle_map + ", rank: " + battle_rank +
              ", Trophies: " + str(battle_trophy) + ", trophies started with: " + trophies_start +
              ", champion played: " + champ_played)"""
        testing.googlesheet.add_data(player, data)


# WORKS