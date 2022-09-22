
import pyautogui as ti 
import webbrowser as wb
import time

n = int(input("Enter number of messages: "))
k = input("Enter the name of contact or group or phone number that you have already texted: ")

msedge_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
#you can use any browser as you want by changing the path but you can use edge as default
url="web.whatsapp.com"
wb.register("msedge",None,wb.BackgroundBrowser(msedge_path))
wb.get("msedge").open_new_tab(url)

time.sleep(15)

ti.click(x=261, y=84)
ti.write(k)


time.sleep(1)

ti.click(x=230, y=350)
#ti.hotkey('ctrl', 's')

#ti.click(x=620, y=950)
ti.click(x=786, y=955)
ti.click(x=910, y=730 ,clicks=n)
