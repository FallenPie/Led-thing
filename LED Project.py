import RPi.GPIO as GPIO
from tkinter import *
import tkinter.font
import time
import math

win=Tk()
GPIO.setmode(GPIO.BOARD)
lis = [8, 10, 12, 16, 18, 22, 24, 26, 32]

light = 9
blinks = 1
ello = StringVar()
ello.set(str(blinks))

def hello():
    beta = 0
    for i in range (light):
        GPIO.setup(lis[beta],GPIO.OUT)
        GPIO.output(lis[beta], True)
        beta+=1
        
    return ledtoggle()

def Down():
    global blinks
    if blinks == 1:
        return
    else:
        blinks-=1
        ello.set(str(blinks))
        win.update_idletasks()
    
def Up():
    global blinks
    blinks+=1
    ello.set(str(blinks))
    win.update_idletasks()

def ledtoggle():
    for i in range (blinks):
        alpha = 0
        for i in range (light):
            GPIO.output(lis[alpha], False)
            time.sleep(0.5)
            GPIO.output(lis[alpha], True)
            time.sleep(0.1)
            alpha+=1
    GPIO.cleanup()
    win.destroy()

win.title("GPIO light blinks")
myfont=tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")
Label(win, text="How many blinks? ").grid(row=0)
Button(win, text="+", command=Up).grid(row=0, column=1)
Button(win, text="-", command=Down).grid(row=0, column=2)
Label(win, text=" %d " %blinks, textvariable=ello).grid(row=0, column=3)
Button(win, text="Run", command=hello).grid(row=0, column=4)

win.mainloop()
