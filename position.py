import pyautogui
try:
    while True:
        x,y=pyautogui.position()
        pos="X:"+str(x).rjust(7)+" Y:"+str(y).rjust(7)
        print(pos,end='')
        print("\b"*len(pos),end='',flush=True)
except KeyboardInterrupt:
    print('\n')
    
    #run this program to get co-ordinates of x and y 
