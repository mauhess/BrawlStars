import requests
import soloShowdown
import duoShowdown
import three_vs_three
import googlesheet

CONC_Modus = ["#L8VURLLP", 0]  # tag, google-sheet-id
UTrash = ["#PGCVYLG9Y", 543582620]  # tag, google-sheet-id
joel = ["#LQ92Q9PR", 1776203116]


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
    first_timestamp_gsheet = googlesheet.get_first_timestamp(player)
    first_timestamp_battlelog = response["items"][0]["battleTime"]
    first_timestamp_battlelog = first_timestamp_battlelog[0:4] + "-" + first_timestamp_battlelog[4:6] \
                                + "-" + first_timestamp_battlelog[6:8] + " " \
                                + first_timestamp_battlelog[9:11] + ":" \
                                + first_timestamp_battlelog[11:13] \
                                + ":" + first_timestamp_battlelog[13:]
    first_timestamp_battlelog = [[str(first_timestamp_battlelog)]]
    if first_timestamp_battlelog == first_timestamp_gsheet:
        print("no new battles")
    else:
        timestamps = googlesheet.get_timestamps(player)  # gets all timestamps of stored battles
        for i in range(24, -1, -1):
            battle_time = response["items"][i]["battleTime"]
            battle_time = battle_time[0:4] + "-" + battle_time[4:6] + "-" + battle_time[6:8] + " " \
                          + battle_time[9:11] + ":" + battle_time[11:13] + ":" + battle_time[13:]
            bt = [str(battle_time)]
            if not (bt in timestamps):
                if response["items"][i]["event"]["id"] != 0:
                    battle_mode = response["items"][i]["battle"]["mode"]
                    if battle_mode == "soloShowdown":
                        soloShowdown.main(response["items"][i], player, battle_time)
                    elif battle_mode == "duoShowdown":
                        duoShowdown.main(response["items"][i], player, battle_time)
                    elif battle_mode == "gemGrab":
                        three_vs_three.main(response["items"][i], player, battle_time)
                    elif battle_mode == "knockout":
                        three_vs_three.main(response["items"][i], player, battle_time)
                    elif battle_mode == "bounty":
                        three_vs_three.main(response["items"][i], player, battle_time)
                    elif battle_mode == "hotZone":
                        three_vs_three.main(response["items"][i], player, battle_time)
                    elif battle_mode == "brawlBall":
                        three_vs_three.main(response["items"][i], player, battle_time)
                    elif battle_mode == "heist":
                        three_vs_three.main(response["items"][i], player, battle_time)
                    else:
                        print(1)


def maurice():
    response = get_response(CONC_Modus[0])
    get_battlelog(CONC_Modus, response)
    response = get_response(UTrash[0])
    get_battlelog(UTrash, response)
    response = get_response(joel[0])
    get_battlelog(joel, response)


def jan():
    response = get_response_jan(CONC_Modus[0])
    get_battlelog(CONC_Modus, response)
    response = get_response_jan(UTrash[0])
    get_battlelog(UTrash, response)
    response = get_response_jan(joel[0])
    get_battlelog(joel, response)


def maurice_hotspot():
    response = get_response_hotspot_maurice(CONC_Modus[0])
    print(response)
    get_battlelog(CONC_Modus, response)
    response = get_response_hotspot_maurice(UTrash[0])
    get_battlelog(UTrash, response)
    response = get_response_hotspot_maurice(joel[0])
    get_battlelog(joel, response)
