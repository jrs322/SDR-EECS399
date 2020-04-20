from tkinter import *
from PIL import Image, ImageTk
from functools import partial
from file_browser import radio_file_browser

class RadioGUI():

    current_screen = "home"
    current_file_page = 0
    file_type = "Folder"
    
    def __init__(self):
        self.current_screen = "Home"
        self.current_file_page = 0
        self.initialize()
        self.canvas_setup()
        self.file_browser = radio_file_browser()
        
    def canvas_setup(self):
        self.root = Tk()
        self.root.title("LOW COST SDR")
        self.canvas = Canvas(root, width = 100, height = 518)
        self.canvas.pack()
        self.img = ImageTk.PhotoImage(Image.open("nokia,jpg"))
        self.canvas.create_image(1, 1, anchor=NW, image =self.img)
    
    def draw_screen(self, text):
        options = Label(root, text=text, height=4, width=11, bg='#8c8868')
        self.canvas.create_window(88, 222, window=options)
    
    def display_files(self, files):
        filler_needed = len(files)//3
        for i in range(0, filler_needed):
            files.append(" ")
        text = " 1. {}  \n 2. {}  \n 3. {}  ".format(files[(currentFilesPage*3)],
                                                     files[(currentFilesPage*3)+1],
                                                     files[(currentFilesPage*3)+2])
        self.draw_screen(text)
    
    def play_station(self, frequency, sample_rate, gain=0):
        return None
    
    def button_handler(self, press):
        if(self.current_screen = "Home"):
            
        elif(self.current_screen = "FM"):
        
        elif(self.current_screen = "Digital"):
            
        elif(self.current_screen = "Playing"):
           
    def button_handler_2(self, press):
        if(press = "1"):
                
        elif(press = "2"):
            
        elif(press = "3"):
            
    def initialize_buttons(self):
        b1 = Button(root, text = "1", command = partial(button_handler, "1"), height=1, width=3)
        self.canvas.create_window(27,348, anchor=NW, window=b1)
        #b2
        b2 = Button(root, text = "2", command = partial(button_handler, "2"), height=1, width=3)
        self.canvas.create_window(75,348, anchor=NW, window=b2)
        #b3
        b3 = Button(root, text = "3", command = partial(button_handler, "3"), height=1, width=3)
        self.canvas.create_window(122,348, anchor=NW, window=b3)
        #previous button
        pB = Button(root, text = "<-", command = partial(button_handler, "p"))
        self.canvas.create_window(128,280, anchor=NW, window=pB)
        #next button
        nB = Button(root, text = "->", command = partial(button_handler, "n"))
        self.canvas.create_window(122,313, anchor=NW, window=nB)


