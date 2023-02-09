import requests
import functions
import testing.soloShowdown
import testing.googlesheet
global response
CONC_Modus = ["#L8VURLLP", 0] # tag, google-sheet-id
UTrash = ["#PGCVYLG9Y", 543582620] # tag, google-sheet-id

def get_response(tag):
    url = 'https://api.brawlstars.com/v1/players/%23'+tag[1: ]+'/battlelog'
    print(url)
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY5NTE5YmZmLTAwZjMtNDExNC1iMzQzLWM5ZmM2NjQ3MTM3MSIsImlhdCI6MTY3NTcxMDgyMCwic3ViIjoiZGV2ZWxvcGVyL2I5OGExYTljLTYzYzctYjJiMS04ZTcxLWU2NDcxNWRlYzg0NSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTg4LjYxLjE3Ni4yMTciXSwidHlwZSI6ImNsaWVudCJ9XX0.wk6HfuFFFclQIzQ-gkYip1ckvT13h4VCthv05YijkPI04k5zPZmj8DugOXe1HC_TDB_suW027AsTdhrFt--faA',
    }
    return requests.get(url, headers=headers).json()


def get_from_battle(i, value):
    return response["items"][i]["battle"][value]

def search_player_duo(i, tag):
    for j in range(5):
        if response["items"][i]["battle"]["teams"][j][0]["tag"] == tag:
            return response["items"][i]["battle"]["teams"][j][0]
        if response["items"][i]["battle"]["teams"][j][1]["tag"] == tag:
            return response["items"][i]["battle"]["teams"][j][1]
    return -1

def get_battlelog(player):
    for i in range(25):
        print("Index: " + str(i))
        testing.soloShowdown.main(response, player, i)
        """
        battle_mode = get_from_battle(i, "mode")
        battle_type = get_from_battle(i, "type")
        battle_rank = str(get_from_battle(i, "rank"))
        battle_map = response["items"][i]["event"]["map"]
        player_infos = "x"
        if battle_mode == "duoShowdown":
            player_infos = search_player_duo(i, player[0])
        champ_played = player_infos["brawler"]["name"]
        trophies_start = str(player_infos["brawler"]["trophies"])
        try:
            battle_trophy = str(get_from_battle(i, "trophyChange"))
        except:  # no trophy change
            battle_trophy = "0"

        if i < 9:
            if int(battle_trophy) < 0:
                print("0" + str(
                    i + 1) + ": " + battle_mode + "_" + battle_type + ", map: " + battle_map + ", rank: " + battle_rank + ", Trophies: " + str(
                    battle_trophy) + ", trophies started with: " + trophies_start + ", champion played: " + champ_played)
            else:
                print("0" + str(
                    i + 1) + ": " + battle_mode + "_" + battle_type + ", map: " + battle_map + ", rank: " + battle_rank + ", Trophies:  " + str(
                    battle_trophy) + ", trophies started with: " + trophies_start + ", champion played: " + champ_played)
        else:
            if int(battle_trophy) < 0:
                print(
                    str(i + 1) + ": " + battle_mode + "_" + battle_type + ", map: " + battle_map + ", rank: " + battle_rank + ", Trophies: " + str(
                        battle_trophy) + ", trophies started with: " + trophies_start + ", champion played: " + champ_played)
            else:
                print(
                    str(i + 1) + ": " + battle_mode + "_" + battle_type + ", map: " + battle_map + ", rank: " + battle_rank + ", Trophies:  " + str(
                        battle_trophy) + ", trophies started with: " + trophies_start + ", champion played: " + champ_played)
"""

try:
    response = get_response(CONC_Modus[0])
    get_battlelog(CONC_Modus)
except:
    response = get_response(UTrash[0])
    get_battlelog(UTrash)





