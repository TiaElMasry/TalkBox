# This is prototype 2 for Talkbox

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter import PhotoImage
import tkinter.font as tkFont
import time
import espeak
from espeak import espeak
import mysql.connector as mysql

LARGEFONT = ("Verdana", 15)

db = mysql.connect(
    host ="a2plcpnl0371.prod.iad2.secureserver.net",
    user = "zbadawi99",
    passwd ="talkBox",
    database ="talkBox"
)

cursor = db.cursor()

class TalkBox(tk.Tk):
     
    # __init__ function for class TalkBox 
    def __init__(self): 
         
        # __init__ function for class Tk
        tk.Tk.__init__(self)
         
        # creating a container
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {}
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (HomePage, Home, Phrases):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # HomePage, Home devices and Simple Phrases respectively with 
            # for loop
            self.frames[F] = frame 
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(HomePage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.refresh()
        frame.tkraise()

# first window frame HomePage
  
class HomePage(tk.Frame):
    global photo1
    global photo2
    def __init__(self, parent, controller): 
        self.buttonList=[]
        self.last_state = 0
        tk.Frame.__init__(self, parent)
        photo1 = PhotoImage(file = "HomeDevicesPic.gif")
        photo1 = photo1.subsample(3,3)
        Style = tkFont.Font(family = "Verdana", size = 15)
        #ttk.Style().configure("TButton", padding=6, relief="flat", background="#000")
        button1 = ttk.Button(self, text ="Talk to devices", image = photo1, compound = BOTTOM,
        command = lambda : controller.show_frame(Home))
        self.buttonList.append(button1)
        button1.focus()
        button1.image = photo1
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        photo2 = PhotoImage(file = "SimplePhrasesPic.gif")
        photo2 = photo2.subsample(3,3)
        button2 = ttk.Button(self, text ="Talk to people", image = photo2, compound = BOTTOM,
        command = lambda : controller.show_frame(Phrases))
        self.buttonList.append(button2)
        button2.image = photo2
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 1, column = 2, padx = 10, pady = 10)

        self.bind_keys(button1)
        self.bind_keys(button2)

    def change(self, event):  
        if self.last_state == 0:
            self.last_state = 1
            self.buttonList[1].focus()
        else:
            self.last_state = 0
            self.buttonList[0].focus()
        
    def right(self, event):
        row = self.buttonList
        targetIndex = (row.index(event.widget)+1) % len(row)
        btnTarget = self.buttonList[targetIndex]
        btnTarget.focus() 

    def refresh(self):
        self.buttonList[0].focus()

    def bind_keys(self, button):
        button.bind("<Left>", self.change)
        button.bind("<Right>", self.change)
        button.bind("<Return>", lambda event : event.widget.invoke())
  
class BaseFrame(tk.Frame):
    
    def __init__(self, parent, controller):
        self.current_row = 0
        self.current_column = 0
        self.last_state = 0
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text = self.label_text,)
        label.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.buttons = []
        self.curBut = [-1,-1]
        self.buttonL = [[]]
        self.varRow = 0
        self.make_nav_buttons(controller)
        self.scrollbar = ttk.Scrollbar(self, orient='horizontal')
        

    def read_file(self, file_name):
        records =[]
        if(file_name == "Simple Phrases.txt"):
            querySP = "SELECT PHRASES FROM simplePhrases"
            cursor.execute(querySP)
            records = cursor.fetchall()
        elif(file_name == "Home Devices.txt"):
            queryHD = "SELECT Phrase FROM homeDevices"
            cursor.execute(queryHD)
            records = cursor.fetchall()
        data ={}
        for i in range(len(records)):
            data[i+1]=records[i]
        #with open(file_name) as f:
        #    data = {i: line.strip() for i,line in enumerate(f, 1)}
        varColumn = 0
        
        for i, name in data.items():
            ttk.Style().configure("TButton", padding=6, relief="flat", background="#000")
            button = ttk.Button(self, text = name,
                                command = lambda name = name: self.speak_out_loud(name))
            
            self.buttonL[self.varRow].insert(varColumn, button)
            button.grid(row = self.varRow, column = varColumn, padx = 10, pady = 10)
            self.buttons.append(button)
            self.bind_keys(button)
            
            varColumn +=1

        if self.buttonL and self.buttonL[0]:
            self.buttonL[0][0].focus()
    

    def clean_up(self):
        for i in self.buttons:
            i.destroy()
        self.buttons = []

    def refresh(self):
        self.clean_up()
        self.read_file(self.file_name)


    def speak_out_loud(self, text):
        ''' change to espeak
        '''
        messagebox.showinfo(message=text)
    
    def bind_keys(self, button):
        button.bind("<Left>", lambda event : self.change(event, "left"))
        button.bind("<Right>", lambda event : self.change(event, "right"))
        button.bind("<Down>", lambda event : self.change(event, "vertical"))
        button.bind("<Return>", lambda event : event.widget.invoke())
        

    def make_nav_buttons(self, controller):
        b = self.nav_buttons = []
        # button to show frame 2 with text
        # layout2
        button = ttk.Button(self, text = self.other_label,
                            command = lambda : controller.show_frame(self.other_frame))
        b.append(button)
     
        # putting the button in its place 
        # by using grid
        self.bind_keys(button)
        button.grid(row = 3, column = 0, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button = ttk.Button(self, text = "Home Page",
                            command = lambda : controller.show_frame(HomePage))
     
        # putting the button in its place by 
        # using grid
        self.bind_keys(button)
        
        button.grid(row = 3, column = 1, padx = 10, pady = 10)

        b.append(button)
 
    def change(self, event, direction):
        if direction == "vertical":
            if self.current_row == 0:
                self.current_row = 1
                if self.current_column > 1:
                    self.current_column = 1
                self.nav_buttons[self.current_column].focus()
            else:
                self.current_row = 0
                self.buttons[self.current_column].focus()
        elif direction == "left":
            if self.current_row == 0:
                b = self.buttons
            else:
                b = self.nav_buttons
            col = self.current_column = (self.current_column - 1) % len(b)
            b[col].focus()
        elif direction == "right":
            if self.current_row == 0:
                b = self.buttons
            else:
                b = self.nav_buttons
      
            col = self.current_column = (self.current_column + 1) % len(b)
            b[col].focus()


# second window frame Home
class Home(BaseFrame):

    def __init__(self, parent, controller):
        self.other_label = "Talk to people"
        self.other_frame = Phrases
        self.file_name = "Home Devices.txt"
        self.label_text = "Talk to devices"
        super().__init__(parent, controller)

            
# third window frame Phrases
class Phrases(BaseFrame): 
    
    def __init__(self, parent, controller):
        self.other_label = "Talk to devices"
        self.other_frame = Home
        self.file_name = "Simple Phrases.txt"
        self.label_text = "Talk to people"
        super().__init__(parent, controller)
  
  
def main():
    app = TalkBox()
    app.geometry("400x250")
    app.mainloop()

if __name__ == "__main__":
    main()
