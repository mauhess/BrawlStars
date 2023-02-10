import requests
import testing.soloShowdown
import testing.duoShowdown
import testing.three_vs_three
import testing.googlesheet
import time
response = 0
CONC_Modus = ["#L8VURLLP", 0] # tag, google-sheet-id
UTrash = ["#PGCVYLG9Y", 543582620] # tag, google-sheet-id

def get_response_jan(tag):
    url = 'https://api.brawlstars.com/v1/players/%23'+tag[1: ]+'/battlelog'
    #print(url)
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImNkMDkwZGRmLTE1ZjItNGIyZi1hYjEwLWYzZDdhODkwOTg4MCIsImlhdCI6MTY3NjAzODE5MCwic3ViIjoiZGV2ZWxvcGVyL2I5OGExYTljLTYzYzctYjJiMS04ZTcxLWU2NDcxNWRlYzg0NSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMjEyLjIwMy41MS4zMyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.Ew4e361Vhlj5YSD5gzXKNyIW5ZOCyD_23AAEl6RDZhdgiTcSGKzJY-hTv8bLnwWgul-hW9vldw1zFK3dgD5hUA',
    }
    return requests.get(url, headers=headers).json()

def get_response(tag):
    url = 'https://api.brawlstars.com/v1/players/%23'+tag[1: ]+'/battlelog'
    #print(url)
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY5NTE5YmZmLTAwZjMtNDExNC1iMzQzLWM5ZmM2NjQ3MTM3MSIsImlhdCI6MTY3NTcxMDgyMCwic3ViIjoiZGV2ZWxvcGVyL2I5OGExYTljLTYzYzctYjJiMS04ZTcxLWU2NDcxNWRlYzg0NSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTg4LjYxLjE3Ni4yMTciXSwidHlwZSI6ImNsaWVudCJ9XX0.wk6HfuFFFclQIzQ-gkYip1ckvT13h4VCthv05YijkPI04k5zPZmj8DugOXe1HC_TDB_suW027AsTdhrFt--faA',
    }
    return requests.get(url, headers=headers).json()



def get_battlelog(player, response):
    timestamps = testing.googlesheet.get_timestamps(player) # gets all timestamps of stored battles
    for i in range(25):
        battle_time = response["items"][i]["battleTime"]
        battle_time = battle_time[0:4] + "-" + battle_time[4:6] + "-" + battle_time[6:8] + " " + battle_time[9:11] + ":" + battle_time[11:13] + ":" + battle_time[13:]
        bt = [str(battle_time)]
        if not(bt in timestamps):
            if (response["items"][i]["event"]["id"] != 0):
                batte_mode = response["items"][i]["battle"]["mode"]
                match batte_mode:
                    case "soloShowdown":
                        testing.soloShowdown.main(response, player, i)
                        #print("Index: " + str(i) + " stored in Excel")
                    case "duoShowdown":
                        testing.duoShowdown.main(response, player, i)
                        #print("Index: " + str(i) + " stored in Excel")
                    case "gemGrab":
                        testing.three_vs_three.main(response, player, i)
                    case "knockout":
                        testing.three_vs_three.main(response, player, i)
                    case "bounty":
                        testing.three_vs_three.main(response, player, i)
                    case "hotZone":
                        testing.three_vs_three.main(response, player, i)
                    case "brawlBall":
                        testing.three_vs_three.main(response, player, i)
                    case "heist":
                        testing.three_vs_three.main(response, player, i)





def main_maurice():
    response = get_response(CONC_Modus[0])
    get_battlelog(CONC_Modus, response)
    response = get_response(UTrash[0])
    get_battlelog(UTrash, response)
def main_jan():
    response = get_response_jan(CONC_Modus[0])
    get_battlelog(CONC_Modus, response)
    response = get_response_jan(UTrash[0])
    get_battlelog(UTrash, response)

main_jan()
#main_maurice()
print(time.process_time())



