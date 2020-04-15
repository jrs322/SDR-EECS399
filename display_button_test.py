# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:29:34 2020

@author: Derek Clontz
"""
from tkinter import *
from PIL import ImageTk, Image, ImageDraw, ImageFont

screen_number = 0
selection_number = 0
area = None
#Selection Box Coordinates
sbx1 = 15
sbx2 = 625
sby1 = 78
sby2 = 148

#Method for outputting screens depending on the input and current state
def create_screen(command=None):
    
    #Current state of screen and selection box are needed to determine next state
    global screen_number
    global selection_number
    global area
    global sbx1
    global sbx2
    global sby1
    global sby2
    
    #Screen parameters are initialized before the screen is drawn
    
    #Set screen to Home Screen
    if(command == "home"):
        screen_number = 0
        selection_number = 0
        sby1 = 78
        sby2 = 148
    
    #Set screen to Signal Type Screen
    if(command == "select"):
        if(screen_number != 1):
            screen_number += 1
            sby1 = 78
            sby2 = 148
            if(selection_number == 0):
                area = "Cleveland"
            if(selection_number == 1):
                area = "Pittsburgh"
    
    #Up command
    if(command == "up"):
        if(selection_number != 0):
            selection_number -= 1
            sby1 -= 80
            sby2 -= 80
    
    #Down command
    if(command == "down"):
        if(selection_number != 1):
            selection_number += 1
            sby1 += 80
            sby2 += 80
            
    #Back command
    if(command == "back"):
        if(screen_number != 0):
            screen_number -= 1
    
    #Initialize new window to hold image
    window = Toplevel(root)
    canvas = Canvas(window, width=640, height=373)
    canvas.pack()
    image = Image.new('RGB', (640, 373), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    ##### Draws screen based on above parameters #####
    
    #Home Screen (Initial)
    if(screen_number == 0):
        headerFont = ImageFont.truetype("TNRB.ttf", 35)
        draw.text((15, 10), "Choose your area...", font=headerFont, fill=(0, 0, 0))
        font = ImageFont.truetype("TNRB.ttf", 60)

        draw.text((175, 75), "Cleveland", font=font, fill=(0, 0, 0))
        draw.text((175, 150), "Pittsburgh", font=font, fill=(0, 0, 0))

        # outline rectangle
        draw.rectangle([10, 10, 630, 363], fill=None, outline="black")

        # button box lines
        draw.line([10, 73, 630, 73], fill="black", width=0)
        draw.line([10, 153, 630, 153], fill="black", width=0)
        draw.line([10, 233, 630, 233], fill="black", width=0)
    
        #Selection box rectangle
        draw.rectangle([sbx1, sby1, sbx2, sby2], fill=None, outline="black", width=3)
    
        
    #Signal Type Screen (Selection Box is set on first option)
    if(screen_number == 1):
        if(area == "Cleveland"):
            headerFont = ImageFont.truetype("TNRB.ttf", 35)
            draw.text((15, 10), "Selected: Cleveland", font=headerFont, fill=(0, 0, 0))
            font = ImageFont.truetype("TNRB.ttf", 60)

            draw.text((175, 75), "Digital", font=font, fill=(0, 0, 0))
            draw.text((175, 150), "Analog", font=font, fill=(0, 0, 0))

            # outline rectangle
            draw.rectangle([10, 10, 630, 363], fill=None, outline="black")

            # button box lines
            draw.line([10, 73, 630, 73], fill="black", width=0)
            draw.line([10, 153, 630, 153], fill="black", width=0)
            draw.line([10, 233, 630, 233], fill="black", width=0)
    
            #Selection box rectangle
            draw.rectangle([sbx1, sby1, sbx2, sby2], fill=None, outline="black", width=3)
        if(area == "Pittsburgh"):
            headerFont = ImageFont.truetype("TNRB.ttf", 35)
            draw.text((15, 10), "Selected: Pittsburgh", font=headerFont, fill=(0, 0, 0))
            font = ImageFont.truetype("TNRB.ttf", 60)

            draw.text((175, 75), "Digital", font=font, fill=(0, 0, 0))
            draw.text((175, 150), "Analog", font=font, fill=(0, 0, 0))

            # outline rectangle
            draw.rectangle([10, 10, 630, 363], fill=None, outline="black")

            # button box lines
            draw.line([10, 73, 630, 73], fill="black", width=0)
            draw.line([10, 153, 630, 153], fill="black", width=0)
            draw.line([10, 233, 630, 233], fill="black", width=0)
    
            #Selection box rectangle
            draw.rectangle([sbx1, sby1, sbx2, sby2], fill=None, outline="black", width=3)
        
    img = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=NW, image=img)
    mainloop() 
        

#Initialize button winow
root = Tk()

#Create frame to contain buttons
frame = Frame(root, bd=10, bg="yellow")
frame.pack()

#Home button
home_button = Button(frame, height=5, width=20, text="Open Home Screen", command=lambda:create_screen("home"))
home_button.grid(row=0, columnspan=2, sticky=W+E)

#Up Button
up = Button(frame, height=5, width=20, text="UP", command=lambda:create_screen("up"))
up.grid(row=1, column=0)

#Down Button
down = Button(frame, height=5, width=20, text="DOWN", command=lambda:create_screen("down"))
down.grid(row=1, column=1)

select = Button(frame, height=5, width=20, text="SELECT", command=lambda:create_screen("select"))
select.grid(row=2, column=0)

clear = Button(frame, height=5, width=20, text="BACK", command=lambda:create_screen("back"))
clear.grid(row=2, column=1)

exitButton = Button(frame, height=5, width=20, text="Exit", command=root.destroy)
exitButton.grid(row=3, columnspan=2, sticky=W+E)

root.mainloop()

