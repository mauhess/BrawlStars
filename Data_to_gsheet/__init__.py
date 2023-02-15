import requests
import Data_to_gsheet.soloShowdown
import Data_to_gsheet.duoShowdown
import Data_to_gsheet.three_vs_three
import Data_to_gsheet.googlesheet

CONC_Modus = ["#L8VURLLP", 0]  # tag, google-sheet-id
UTrash = ["#PGCVYLG9Y", 543582620]  # tag, google-sheet-id


def get_response_jan(tag):
    url = 'https://api.brawlstars.com/v1/players/%23' + tag[1:] + '/battlelog'
    # print(url)
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImNkMDkwZGRmLTE1ZjItNGIyZi1hYjEwLWYzZDdhODkwOTg4MCIsImlhdCI6MTY3NjAzODE5MCwic3ViIjoiZGV2ZWxvcGVyL2I5OGExYTljLTYzYzctYjJiMS04ZTcxLWU2NDcxNWRlYzg0NSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMjEyLjIwMy41MS4zMyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.Ew4e361Vhlj5YSD5gzXKNyIW5ZOCyD_23AAEl6RDZhdgiTcSGKzJY-hTv8bLnwWgul-hW9vldw1zFK3dgD5hUA',
    }
    return requests.get(url, headers=headers).json()


def get_response(tag):
    url = 'https://api.brawlstars.com/v1/players/%23' + tag[1:] + '/battlelog'
    # print(url)
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY5NTE5YmZmLTAwZjMtNDExNC1iMzQzLWM5ZmM2NjQ3MTM3MSIsImlhdCI6MTY3NTcxMDgyMCwic3ViIjoiZGV2ZWxvcGVyL2I5OGExYTljLTYzYzctYjJiMS04ZTcxLWU2NDcxNWRlYzg0NSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTg4LjYxLjE3Ni4yMTciXSwidHlwZSI6ImNsaWVudCJ9XX0.wk6HfuFFFclQIzQ-gkYip1ckvT13h4VCthv05YijkPI04k5zPZmj8DugOXe1HC_TDB_suW027AsTdhrFt--faA',
    }
    return requests.get(url, headers=headers).json()


def get_response_hotspot_maurice(tag):
    url = 'https://api.brawlstars.com/v1/players/%23' + tag[1:] + '/battlelog'
    # print(url)
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjZlZTQwMjBhLWE1ZjktNDdiNS1iOTEwLWI1MWNhNDllZTkyYSIsImlhdCI6MTY3NjMwMjYzNiwic3ViIjoiZGV2ZWxvcGVyL2I5OGExYTljLTYzYzctYjJiMS04ZTcxLWU2NDcxNWRlYzg0NSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTc4LjE5Ny4yMDkuMjQ5Il0sInR5cGUiOiJjbGllbnQifV19.9miGOh6JCU0LFWE63aPxZTO0fcQ5neU0CEd5iDrP_psFeYz-g63rnVb9W5bZBEJRSC7YZrTmAaSed2bBK7o3YA',
    }
    return requests.get(url, headers=headers).json()


def get_battlelog(player, response):
    first_timestamp_gsheet = Data_to_gsheet.googlesheet.get_first_timestamp(player)
    first_timestamp_battlelog = response["items"][0]["battleTime"]
    first_timestamp_battlelog = first_timestamp_battlelog[0:4] + "-" + first_timestamp_battlelog[4:6] \
                                + "-" + first_timestamp_battlelog[6:8] + " " \
                                + first_timestamp_battlelog[9:11] + ":" \
                                + first_timestamp_battlelog[11:13] \
                                + ":" + first_timestamp_battlelog[13:]
    first_timestamp_battlelog = [[str(first_timestamp_battlelog)]]
    if (first_timestamp_battlelog == first_timestamp_gsheet):
        print("keine neuen Kämpfe")
    else:
        timestamps = Data_to_gsheet.googlesheet.get_timestamps(player)  # gets all timestamps of stored battles
        for i in range(24, -1, -1):
            battle_time = response["items"][i]["battleTime"]
            battle_time = battle_time[0:4] + "-" + battle_time[4:6] + "-" + battle_time[6:8] + " " \
                          + battle_time[9:11] + ":" + battle_time[11:13] + ":" + battle_time[13:]
            bt = [str(battle_time)]
            if not (bt in timestamps):
                if (response["items"][i]["event"]["id"] != 0):
                    battle_mode = response["items"][i]["battle"]["mode"]
                    match battle_mode:
                        case "soloShowdown":
                            Data_to_gsheet.soloShowdown.main(response["items"][i], player, battle_time)
                        case "duoShowdown":
                            Data_to_gsheet.duoShowdown.main(response["items"][i], player, battle_time)
                        case "gemGrab":
                            Data_to_gsheet.three_vs_three.main(response["items"][i], player, battle_time)
                        case "knockout":
                            Data_to_gsheet.three_vs_three.main(response["items"][i], player, battle_time)
                        case "bounty":
                            Data_to_gsheet.three_vs_three.main(response["items"][i], player, battle_time)
                        case "hotZone":
                            Data_to_gsheet.three_vs_three.main(response["items"][i], player, battle_time)
                        case "brawlBall":
                            Data_to_gsheet.three_vs_three.main(response["items"][i], player, battle_time)
                        case "heist":
                            Data_to_gsheet.three_vs_three.main(response["items"][i], player, battle_time)


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


def main_maurice_hotspot():
    response = get_response_hotspot_maurice(CONC_Modus[0])
    get_battlelog(CONC_Modus, response)
    response = get_response_hotspot_maurice(UTrash[0])
    get_battlelog(UTrash, response)


# main_maurice_hotspot()
# main_jan()
main_maurice()
