global response
import Data_to_Excel.googlesheet

def get_from_battle(i, value, response):
    return response["items"][i]["battle"][value]

def main(response, player, i):
    battle_time = response["items"][i]["battleTime"]
    battle_time = battle_time[0:4] + "-" + battle_time[4:6] + "-" + battle_time[6:8] + " " + battle_time[9:11] + ":" + battle_time[11:13] + ":" + battle_time[13:]
    bt = [str(battle_time)]
    timestamps = Data_to_Excel.googlesheet.get_timestamps(player) # gets all timestamps of stored battles
    if not(bt in timestamps): # checks if battle is already in excel file
        battle_id = response["items"][i]["event"]["id"]
        battle_mode = get_from_battle(i, "mode", response)
        battle_type = get_from_battle(i, "type", response)
        battle_result = get_from_battle(i, "result", response)
        battle_map = response["items"][i]["event"]["map"]
        player_battle_infos = "__xx__"
        player_team = "__xx__"
        player_nr = -99
        for j in range(2):
            for k in range(3):
                if response["items"][i]["battle"]["teams"][j][k]["tag"] == player[0]:
                    player_battle_infos = response["items"][i]["battle"]["teams"][j][k]
                    player_team = response["items"][i]["battle"]["teams"][j]
                    player_nr = k
        champ_played = player_battle_infos["brawler"]["name"]
        trophies_start = str(player_battle_infos["brawler"]["trophies"])
        if (player_nr==0):
            mate_one = player_team[1]
            mate_two = player_team[2]
        elif (player_nr == 1):
            mate_one = player_team[0]
            mate_two = player_team[2]
        else:
            mate_one = player_team[0]
            mate_two = player_team[1]
        mate_one_tag = mate_one["tag"]
        mate_one_champ_player = mate_one["brawler"]["name"]
        mate_two_tag = mate_two["tag"]
        mate_two_champ_player = mate_two["brawler"]["name"]
        try:
            battle_trophy = str(get_from_battle(i, "trophyChange", response))
        except:  # no trophy change
            battle_trophy = "0"
        data = [[battle_time, battle_id, battle_mode, battle_type, battle_map, battle_result, champ_played, trophies_start, battle_trophy, mate_one_tag, mate_one_champ_player, mate_two_tag, mate_two_champ_player]]
        Data_to_Excel.googlesheet.add_data(player, data)