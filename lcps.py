from tkinter import *
from PIL import Image, ImageTk
from functools import partial

#### TKINTER CANVAS SETUP ####
root = Tk()
root.title("LOW COST SDR")
canvas = Canvas(root, width = 180, height = 518)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("nokia.jpg"))
canvas.create_image(1,1, anchor=NW, image=img)

#### GLOBAL VARIABLES ####
currentScreen = "home"
currentFilesPage = 0
currentPath = ""

#### SCREEN DRAWING ####
def draw_screen(text):
    global currentScreen
    options = Label(root, text = text, height=4, width=11, bg='#8c8868')
    canvas.create_window(88, 222, window=options)

#### HOME SCREEN, RESET PLAYBACK HERE ####
def home():
    global currentScreen, currentPath, currentFilesPage
    currentScreen = "home"
    currentPath = ""
    currentFilesPage = 0
    display_files()
    #end playback

#### DISPLAYING FILES FOR FM AND DIGITAL BROWSING ####
def display_files():
    global currentScreen, currentPath, currentFilesPage

    # normally this array would be populated from the current path... but
    # for now we'll use a dummy system
    #files = ["SCAN", "FM", "DIGITAL"] # DUMMY SYSTEM
    files = ["OHIO", "PORTLAND", "CLE", "BOSTON", "PITTS", "COLUMBUS"] # DUMMY SYSTEM

    text = " 1. {}  \n 2. {}  \n 3. {}  ".format(files[(currentFilesPage*3)], files[(currentFilesPage*3)+1], files[(currentFilesPage*3)+2])
    draw_screen(text)

#### SELECTION OF FILES ####
def interpret_selection(selnum):
    # if selection is of tsv file then...
    play(3)
    # if selection is of folder type then...
    # append selection to current path
    #display_files()

#### PLAYING TSV FILES WITH PROPER ARGUEMENTS ####
def play(num):
    channelExample = "88.5"
    channelExampleName = "CWRU News"
    text = "{} {}\n{}".format("FM", channelExampleName, channelExample)

    draw_screen(text)

#### BUTTON HANDLING ####
def button_handler(press):
    global currentScreen, currentFM, currentDigital, currentFilesPage

    if(press == "n"):
        currentFilesPage += 1
        display_files()
    elif(press == "p"):
        currentFilesPage -= 1
        display_files()
    else:
        interpret_selection(press)

#### START UP DEVICE ####
def initilize():

    #main menu
    display_files()

    #b1
    b1 = Button(root, text = "1", command = partial(button_handler, "1"), height=1, width=3)
    canvas.create_window(27,348, anchor=NW, window=b1)

    #b2
    b2 = Button(root, text = "2", command = partial(button_handler, "2"), height=1, width=3)
    canvas.create_window(75,348, anchor=NW, window=b2)

    #b3
    b3 = Button(root, text = "3", command = partial(button_handler, "3"), height=1, width=3)
    canvas.create_window(122,348, anchor=NW, window=b3)

    #previous button
    pB = Button(root, text = "<-", command = partial(button_handler, "p"))
    canvas.create_window(128,280, anchor=NW, window=pB)

    #next button
    nB = Button(root, text = "->", command = partial(button_handler, "n"))
    canvas.create_window(122,313, anchor=NW, window=nB)

    #home button
    hB = Button(root, text = "Home", command = home, height=2, width=4)
    canvas.create_window(69,280, anchor=NW, window=hB)

initilize()
root.mainloop()
