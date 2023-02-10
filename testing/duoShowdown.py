global response
import testing.googlesheet

def get_from_battle(i, value, response):
    return response["items"][i]["battle"][value]

def main(response, player, i):
    battle_time = response["items"][i]["battleTime"]
    battle_time = battle_time[0:4] + "-" + battle_time[4:6] + "-" + battle_time[6:8] + " " + battle_time[9:11] + ":" + battle_time[11:13] + ":" + battle_time[13:]
    bt = [str(battle_time)]
    timestamps = testing.googlesheet.get_timestamps(player) # gets all timestamps of stored battles
    if not(bt in timestamps): # checks if battle is already in excel file
        battle_id = response["items"][i]["event"]["id"]
        battle_mode = get_from_battle(i, "mode", response)
        battle_type = get_from_battle(i, "type", response)
        battle_rank = str(get_from_battle(i, "rank", response))
        battle_map = response["items"][i]["event"]["map"]
        player_battle_infos = "__xx__"
        battle_mate = "__XX__"
        for j in range(5):
            if response["items"][i]["battle"]["teams"][j][0]["tag"] == player[0]:
                player_battle_infos = response["items"][i]["battle"]["teams"][j][0]
                battle_mate = response["items"][i]["battle"]["teams"][j][1]
            if response["items"][i]["battle"]["teams"][j][1]["tag"] == player[0]:
                player_battle_infos = response["items"][i]["battle"]["teams"][j][1]
                battle_mate = response["items"][i]["battle"]["teams"][j][0]
        champ_played = player_battle_infos["brawler"]["name"]
        trophies_start = str(player_battle_infos["brawler"]["trophies"])
        battle_mate_tag = battle_mate["tag"]
        battle_mate_brawler = battle_mate["brawler"]["name"]
        try:
            battle_trophy = str(get_from_battle(i, "trophyChange", response))
        except:  # no trophy change
            battle_trophy = "0"
        data = [[battle_time, battle_id, battle_mode, battle_type, battle_map, battle_rank, champ_played, trophies_start, battle_trophy, battle_mate_tag, battle_mate_brawler]]
        testing.googlesheet.add_data(player, data)