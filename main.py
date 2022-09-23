from AppOpener import run
import pyautogui as ti 
import webbrowser as wb
import time


n = int(input("Enter number of messages: "))
k = input("Enter the name of contact or group: ")

run("whatsapp")
time.sleep(15)

#you need to change your positions according to your sticker positions 
ti.click(x=478, y=220)
ti.write(k)

time.sleep(2)
ti.click(x=314, y=501)

ti.hotkey('ctrl', 's')
ti.click(x=1386, y=942 ,clicks=n)


