from functions import *
settings = load_settings()

ip = get('https://api.ipify.org').text

if settings["currentIP"] != ip:
    curLocation = settings["location"]
    print(("Your public IP Address is: " + ip + " in: " + curLocation))
    save_settings(ip)
    sendWhatsMessage("Your public IP Address is: " + ip)
else:
    print("Your current ip is up-to date")
