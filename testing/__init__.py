import requests
import functions
import testing.soloShowdown

#terminal
#curl -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY5NTE5YmZmLTAwZjMtNDExNC1iMzQzLWM5ZmM2NjQ3MTM3MSIsImlhdCI6MTY3NTcxMDgyMCwic3ViIjoiZGV2ZWxvcGVyL2I5OGExYTljLTYzYzctYjJiMS04ZTcxLWU2NDcxNWRlYzg0NSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTg4LjYxLjE3Ni4yMTciXSwidHlwZSI6ImNsaWVudCJ9XX0.wk6HfuFFFclQIzQ-gkYip1ckvT13h4VCthv05YijkPI04k5zPZmj8DugOXe1HC_TDB_suW027AsTdhrFt--faA' https://api.brawlstars.com/v1/players/%23L8VURLLP/battlelog
CONC_Modus_tag = "#L8VURLLP"
UTrash_tag = "#PGCVYLG9Y"
def get_response(tag):
    url = 'https://api.brawlstars.com/v1/players/%23'+tag[1: ]+'/battlelog'
    print(url)
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY5NTE5YmZmLTAwZjMtNDExNC1iMzQzLWM5ZmM2NjQ3MTM3MSIsImlhdCI6MTY3NTcxMDgyMCwic3ViIjoiZGV2ZWxvcGVyL2I5OGExYTljLTYzYzctYjJiMS04ZTcxLWU2NDcxNWRlYzg0NSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTg4LjYxLjE3Ni4yMTciXSwidHlwZSI6ImNsaWVudCJ9XX0.wk6HfuFFFclQIzQ-gkYip1ckvT13h4VCthv05YijkPI04k5zPZmj8DugOXe1HC_TDB_suW027AsTdhrFt--faA',
    }
    return requests.get(url, headers=headers).json()

response = get_response(CONC_Modus_tag)

def get_from_battle(i, value):
    return response["items"][i]["battle"][value]

def search_player_duo(i, tag):
    for j in range(5):
        if response["items"][i]["battle"]["teams"][j][0]["tag"] == tag:
            return response["items"][i]["battle"]["teams"][j][0]
        if response["items"][i]["battle"]["teams"][j][1]["tag"] == tag:
            return response["items"][i]["battle"]["teams"][j][1]
    return -1

def search_player_solo(i, tag):
    for j in range(10):
        if response["items"][i]["battle"]["players"][j]["tag"] == tag:
            return response["items"][i]["battle"]["players"][j]


def get_battlelog(tag):
    for i in range(25):
        print(i)
        testing.soloShowdown.main(response, tag, i)
        battle_mode = get_from_battle(i, "mode")
        battle_type = get_from_battle(i, "type")
        battle_rank = str(get_from_battle(i, "rank"))
        battle_map = response["items"][i]["event"]["map"]
        player = "x"
        if battle_mode == "duoShowdown":
            player = search_player_duo(i, tag)
        if battle_mode == "soloShowdown":
            player = search_player_solo(i, tag)
        champ_played = player["brawler"]["name"]
        trophies_start = str(player["brawler"]["trophies"])
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
#print(functions.duoShowdown())
get_battlelog(CONC_Modus_tag)
#get_battlelog(UTrash_tag)



