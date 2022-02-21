import subprocess
import sys
import json
import datetime


def installRequirements(package):
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-r", package])


def load_settings():
    with open("data.json", "r") as f:
        settings = json.load(f)
        print(settings)
    # f.close()
    return settings


def save_settings(ip):
    with open("data.json", "w") as jsonFile:
        data = load_settings()
        data["currentIP"] = ip
        # print(data)
        #json_object = json.dumps(data, indent=4)
        #json.dumps(data, jsonFile)
        # jsonFile.seek(0)  # rewind
        # jsonFile.write(data)
        # jsonFile.truncate()
    jsonFile.close()


def sendWhatsMessage(whatsMessage):
    settings = load_settings()
    x = datetime.datetime.now()
    curHour = x.hour
    curMinute = x.minute + 2
    whatsNum = settings["whatsNum"]
    try:
        pywhatkit.sendwhatmsg(whatsNum, whatsMessage, curHour, curMinute, 20)
        print("Successfully Sent!")
    except:
        print("An Unexpected Error!")


try:
    from requests import get
    import pywhatkit
except:
    installRequirements("requirements.txt")
    from requests import get
    import pywhatkit
