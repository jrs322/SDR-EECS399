from tkinter import *
from PIL import Image, ImageTk
from functools import partial
from file_browser import radio_file_browser
import time


class RadioGUI():

    current_screen = "home"
    current_file_page = 0
    max_page_limit = 0
    
    def __init__(self):
        self.current_screen = "Home"
        self.current_file_page = 0
        self.file_browser = radio_file_browser()
        self.canvas_setup()
        self.initialize_buttons()
        self.display_files(self.file_browser.get_current_contents())
        self.root.mainloop()
        
        
    def canvas_setup(self):
        self.root = Tk()
        self.root.title("LOW COST SDR")
        self.canvas = Canvas(self.root, width = 200, height = 518)
        self.canvas.pack()
        self.img = ImageTk.PhotoImage(Image.open("nokia.jpg"))
        self.canvas.create_image(1, 1, anchor=NW, image =self.img)
        
    def draw_screen(self, text):
        options = Label(self.root, text=text, height=4, width=11, bg='#8c8868')
        self.canvas.create_window(88, 222, window=options)
    
    def display_files(self, files):
        filler_needed = len(files)%3
        print(filler_needed)
        if filler_needed > 0:
            for i in range(0, 3-filler_needed):
                self.file_browser.current_file_contents.append("N/A")
                print(self.file_browser.current_file_contents)
        max_pages = len(files)/3
        if self.current_file_page > max_pages-1 or 0 > self.current_file_page:
            print("Max or Min limit reached")
            return None
        text = " 1. {}  \n 2. {}  \n 3. {}  ".format(files[(self.current_file_page*3)],
                                                     files[(self.current_file_page*3)+1],
                                                     files[(self.current_file_page*3)+2])
        self.draw_screen(text)
    
    def play_fm(self, frequency, sample_rate, gain=0):
        return None
    
    def play_digital(self, file_name):
        return None
    
    def button_handler(self, press):
        if(self.current_screen == "Home"):
            self.button_handler_home(press)
        elif(self.current_screen == "FM"):
            self.button_handler_radio(press)
        elif(self.current_screen == "Digital"):
            self.button_handler_radio(press)
        elif(self.current_screen == "Playing"):
            self.button_handler_playing(press)
           
    def button_handler_home(self, press):
        if(press == "1"):
            self.file_browser.get_new_path(self.file_browser.current_file_contents[0])
            self.display_files(self.file_browser.get_current_contents())
            self.current_screen = "FM"
        elif(press == "2"):
            self.file_browser.get_new_path(self.file_browser.current_file_contents[1])
            self.display_files(self.file_browser.get_current_contents())
            self.current_screen = "Digital"
            
    def button_handler_radio(self, press):
        if(press == "1" or press == "2" or press == "3" ):
            #need to check files if they are more folders or not
            #if go into a folder reset page count
            self.current_file_page = 0
            print(self.file_browser.current_file_contents)
            if(self.file_browser.current_file_contents[int(press)-1][0:2] == "m_"):
                #set new path display
                self.file_browser.get_new_path(self.file_browser.current_file_contents[int(press)])
                self.display_files(self.file_browser.get_current_contents())
            elif(self.file_browser.current_file_contents[int(press)-1][0:3] == "N/A"):
                print("Doing Nothing")
            else:
                if(self.current_screen == "Digital"):
                    self.play_digital()
                    self.current_screen = "Playing"
                else:
                    self.play_fm()
                    self.current_screen = "Playing"
        elif(press == "n"):
            self.current_file_page+=1
            self.display_files(self.file_browser.get_current_contents())
        elif(press == "p"):
            self.current_file_page-=1
            self.display_files(self.file_browser.get_current_contents())
        elif(press == "Home"):
            self.current_file_page=0
            self.file_browser.go_home()
            self.display_files(self.file_browser.get_current_contents())
            
    def button_handler_playing(self, press):
        if(press == "Home"):
            self.current_file_page=0
            self.file_browser.go_home()
            self.display_files(self.file_browser.get_current_contents())
            
            
    def initialize_buttons(self):
        b1 = Button(self.root, text = "1", command = partial(self.button_handler, "1"), height=1, width=3)
        self.canvas.create_window(27,348, anchor=NW, window=b1)
        #b2
        b2 = Button(self.root, text = "2", command = partial(self.button_handler, "2"), height=1, width=3)
        self.canvas.create_window(75,348, anchor=NW, window=b2)
        #b3
        b3 = Button(self.root, text = "3", command = partial(self.button_handler, "3"), height=1, width=3)
        self.canvas.create_window(122,348, anchor=NW, window=b3)
        #previous button
        pB = Button(self.root, text = "<-", command = partial(self.button_handler, "p"))
        self.canvas.create_window(128,280, anchor=NW, window=pB)
        #next button
        nB = Button(self.root, text = "->", command = partial(self.button_handler, "n"))
        self.canvas.create_window(122,313, anchor=NW, window=nB)
        
        hB = Button(self.root, text = "Home", command = partial(self.button_handler, "Home"))
        self.canvas.create_window(69, 280, anchor=NW, window=hB)

                  
myApp = RadioGUI()