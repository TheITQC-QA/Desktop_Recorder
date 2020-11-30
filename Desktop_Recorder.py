import pyautogui
import time
import datetime
import os

default_name = 1
default_interval = 5

today = datetime.date.today()
current_time = time.strftime("%H:%M:%S", time.localtime())
current_date = today.strftime("%Y/%m/%d")
current_date = current_date.replace("/","_")
current_time = current_time.replace(":","")
create_folder_name = current_date+current_time
os.mkdir("Recordings\{}".format(create_folder_name))
while default_name < 1000000000:  #you can put infinite loop too
    capturedesktop = pyautogui.screenshot()
    default_name = default_name +1
    folderPath = "Recordings\{}\{}.png".format(create_folder_name, default_name)
    #print(folderPath)
    capturedesktop.save(folderPath)
    time.sleep(default_interval)