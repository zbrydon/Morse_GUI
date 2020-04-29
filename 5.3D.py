from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
import time

speedPercent = 100                       
longTime = 30.0 / speedPercent           
shortTime = 10.0 / speedPercent          
intraTime = 10.0 / speedPercent          
spaceTime = 70.0 / speedPercent          
betweenCharTime = 30.0 / speedPercent    
inputString = ""

converted = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.",".":".-.-.-",",":"--..--",":":"---...","?":"..--..","'":".----.","-":"-....-","/":"-..-.","(":"-.--.-",")":"-.--.-","\"":".-..-.","@":".--.-.","=":"-...-","[":"-.--.-","]":"-.--.-","$":"...-..-","+":".-.-.",";":"-.-.-.","_":"..--.-","!":"---."}

##Hardware

led = LED(14)



## GUI DEFINITIONS ##

win = Tk()
win.title("Text to LED Morse Code")
myFont = tkinter.font.Font(family = 'Helvetica' , size = 12, weight = "bold")

##Event functions ##

#Flash LED for the dash
def longFlash():
    led.on()
    time.sleep(longTime)
    led.off()

#Flash LED for the period
def shortFlash():
    led.on()
    time.sleep(shortTime)
    led.off()

#Sleep for time of a space
def space():
    time.sleep(spaceTime)

#Ask for input
#returns the input


entry_1 = Entry(win)
entry_1.grid(row = 0, column = 1)

#Make input lowercase and assign it to a variable


def ledToggle():
    inputString = entry_1.get().lower()
    if len(inputString) >= 12:
            print("To many Charaters")
            return 
    #Go through each character of the input
    for c in inputString:
        #If it is a space
        if c == " ":
            space()
        #If it is in the dictionary
        elif c in converted:
            #convert character to the morse code
            morseconverted = converted[c]
            #goes through each character in the morse code
            for symbol in morseconverted:
                #If the symbol is a dash
                if symbol == "-":
                    longFlash()
                    time.sleep(intraTime)
                #If the symbol is a period
                elif symbol == ".":
                    shortFlash()
                    time.sleep(intraTime)
                #If the symbol is somehow not a dash or period
                else:
                    print ("Not a '-' or '.'")
            time.sleep(betweenCharTime)
        #If the character is not supported in the dictionary
        else:
            print ("'" + c + "'" + " is not a supported character")
    #Ask for input again
    inputString = entry_1.get().lower()

def close():
    RPi.GPIO.cleanup()
    win.destroy()
                     

## Widgets ##

    
    
ledRedButton = Button(win, text = 'Start Conversion', font = myFont,command = ledToggle, bg = 'red' , height = 1, width = 24)
ledRedButton.grid(row = 2, column = 1)




exitButton = Button(win , text = 'Exit' , font = myFont , command = close, bg = 'white' , height = 1 , width = 10)
exitButton.grid(row = 4, column = 1)


win.protocol("WM_DELETE_WINDOW" , close)

win.mainloop()