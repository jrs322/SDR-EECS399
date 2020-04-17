from tkinter import *
from PIL import Image, ImageTk

#tkinter canvas setup
root = Tk()
canvas = Canvas(root, width = 180, height = 518)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("nokia.jpg"))
canvas.create_image(1,1, anchor=NW, image=img)

#global variables
currentScreen = "home"
currentFM = 0
currentDigital = 0


#### SCREEN DRAWING ####
def home():
    global currentScreen
    options = Label(root, text = "1.Scan\n2.FM\n3.Digital", height=4, width=11, bg='#8c8868')
    canvas.create_window(88, 222, window=options)
    currentScreen = "home"

def scan():
    global currentScreen
    scanning = Label(root, text = "Scanning\n\n", height=4, width=11, bg='#8c8868')
    scanning.pack()
    canvas.create_window(88, 222, window=scanning)
    currentScreen = "scan"

def fm():
    global currentScreen, currentFM

    #Get channel array and form screen text label
    channels = ["88.5", "101.3", "107.7", "97.9", "102.8", "89.9"]
    text = " 1. {}  \n 2. {}  \n 3. {}  ".format(channels[currentFM], channels[currentFM+1], channels[currentFM+2])

    #Draw screen
    fmListen = Label(root, text = text, height=4, width=11, bg='#8c8868')
    fmListen.pack()
    canvas.create_window(88, 222, window=fmListen)
    currentScreen = "fm"

def digital():
    global currentScreen, currentDigital

    #Get channel array and form screen text label
    channels = ["88.5", "101.3", "107.7", "97.9", "102.8", "89.9"]
    text = " 1. {}  \n 2. {}  \n 3. {}  ".format(channels[currentFM], channels[currentFM+1], channels[currentFM+2])

    #draw screen
    digListen = Label(root, text = "  1. 100  \n  2. 200  \n  3. 300  ", height=4, width=11, bg='#8c8868')
    digListen.pack()
    canvas.create_window(88, 222, window=digListen)
    currentScreen = "digital"


#### BUTTON HANDLING ####
def b1Pressed():
    global currentScreen
    if(currentScreen == "home"):
        scan()

def b2Pressed():
    global currentScreen
    if(currentScreen == "home"):
        fm()

def b3Pressed():
    global currentScreen
    if(currentScreen == "home"):
        digital()

def nPressed():
    global currentScreen, currentFM
    if(currentScreen == "fm"):
        currentFM += 1
        fm()

def pPressed():
    global currentScreen, currentFM
    if(currentScreen == "fm"):
        currentFM -= 1
        fm()


#### START UP DEVICE ####
def initilize():

    #main menu
    home()

    #b1
    b1 = Button(root, text = "1", command = b1Pressed, height=1, width=3)
    canvas.create_window(27,348, anchor=NW, window=b1)

    #b2
    b2 = Button(root, text = "2", command = b2Pressed, height=1, width=3)
    canvas.create_window(75,348, anchor=NW, window=b2)

    #b3
    b3 = Button(root, text = "3", command = b3Pressed, height=1, width=3)
    canvas.create_window(122,348, anchor=NW, window=b3)

    #previous button
    pB = Button(root, text = "<-", command = pPressed)
    canvas.create_window(128,280, anchor=NW, window=pB)

    #next button
    nB = Button(root, text = "->", command = nPressed)
    canvas.create_window(122,313, anchor=NW, window=nB)

    #home button
    hB = Button(root, text = "Home", command = home, height=2, width=4)
    canvas.create_window(69,280, anchor=NW, window=hB)

initilize()
root.mainloop()
