
import RPi.GPIO as GPIO
from tkinter import *
import tkinter.font
from time import sleep
import math

win=Tk()
GPIO.setmode(GPIO.BOARD)
lis = [8, 10, 12, 16, 18, 22, 24, 26, 32]

light = 9
blinks = 1
strblinks = StringVar()
strblinks.set(str(blinks))

def ledsetup():
    i = 0
    for i in range (light):
        GPIO.setup(lis[i],GPIO.OUT)
        GPIO.output(lis[i], True)
        i+=1     
    return ledtoggle()

def Down():
    global blinks
    if blinks == 1:
        return
    else:    
        blinks-=1
        strblinks.set(str(blinks))
        win.update_idletasks()
    
def Up():
    global blinks
    blinks+=1
    strblinks.set(str(blinks))
    win.update_idletasks()

def ledtoggle():
    for i in range (blinks):
        i = 0
        for i in range (light):
            GPIO.output(lis[i], False)
            sleep(0.2)
            GPIO.output(lis[i], True)
            sleep(0.05)
            i+=1
    GPIO.cleanup()
    win.destroy()

def Quit():
    GPIO.cleanup()
    win.destroy()

win.title("GPIO light blinks")

myfont=tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")
Label(win, text="How many blinks? ").grid(row=0)
Button(win, text="+", command=Up).grid(row=0, column=1)
Button(win, text="-", command=Down).grid(row=0, column=2)
Label(win, text=" %d " %blinks, textvariable=strblinks).grid(row=0, column=3)
Button(win, text="Run", command=ledsetup, width=6).grid(row=0, column=4)
Button(win, text="Quit", command=Quit, width=6).grid(row=1, column=4)

win.mainloop()

