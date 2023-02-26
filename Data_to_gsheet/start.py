import main


def start_method():
    try:
        main.maurice()
    except:
        try:
            main.jan()
        except:
            try:
                main.maurice_hotspot()
            except:
                print("fail")

start_method()
