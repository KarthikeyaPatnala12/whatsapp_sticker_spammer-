from AppOpener import run
import pyautogui as ti 
import time


n = int(input("Enter number of messages: "))
k = input("Enter the name of contact or group: ")

run("whatsapp")
time.sleep(15)

#you need to change your positions according to your sticker positions 
ti.click(x=478, y=220) # to open search 
ti.write(k) 

time.sleep(2) #To load search on whatsapp that needs some time 
ti.click(x=314, y=501) #Contact or group name 

ti.hotkey('ctrl', 's') #shortcut for sticker panel 
ti.click(x=1386, y=942 ,clicks=n) 


