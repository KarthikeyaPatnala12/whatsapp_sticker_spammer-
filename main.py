import webbrowser
import pyautogui as ti 
import time
from webbrowser import open
from random import randint


n = int(input("Enter number of messages: "))
k = input("Enter the name of contact or group: ")
n_stickers=int(input("Enter the number of stickers that you are going to add for spamming"))
pos_x=[]    #To store x_coordinates of stickers
pos_y=[]    #To store y_coordinates of stickers
open("https://web.whatsapp.com/")
time.sleep(15)

#Note down the sticker coordinates using this 
#After getting your wished stickers 
#Press ctr+c to stop getting coordintes displayed
#and to proceed
try:
    while True:
        x_i,y_i=ti.position()
        posi="X:"+str(x_i).rjust(7)+" Y:"+str(y_i).rjust(7)
        print(posi,end="")
        print('\b'*len(posi),end="",flush=True)
except KeyboardInterrupt:
    print("\n")
for i in range(n_stickers):
      pos_x.append(int(input(f"x{i+1}:")))
      pos_y.append(int(input(f"y{i+1}:")))

                   

ti.click(x=478, y=220) # to open search 
ti.write(k) 

time.sleep(2) #To load search on whatsapp that needs some time 
ti.click(x=314, y=501) #Contact or group name 
i=0
# while i<n:
#     m=randint(0,len(pos_x)-1)
#     ti.click(x=pos_x[m],y=pos_y[m])
#     i+=1
                   



