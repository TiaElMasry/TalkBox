# This is prototype 2 for Talkbox

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
 
LARGEFONT =("Verdana", 35)
  
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
            # HomePage, Home, devices respectively with 
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
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        photo = PhotoImage(file = "HomeDevicesPic.gif")
        button1 = ttk.Button(self, text ="Home devices", image = photo,
        command = lambda : controller.show_frame(Home))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Simple Phrases",
        command = lambda : controller.show_frame(Phrases))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 1, column = 5, padx = 10, pady = 10)

    def refresh(self):
        pass
  
class BaseFrame(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text = self.label_text,)
        label.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.buttons = []
    
    def read_file(self, file_name):
        with open(file_name) as f:
            data = {i: line.strip() for i,line in enumerate(f, 1)}   
        
        # buttons
        for i, name in data.items():
            button = ttk.Button(self, text = name,
                                command = lambda name = name: self.show_message(name))
            button.grid(row = 2, column = i, padx = 10, pady = 10)
            self.buttons.append(button)

    def clean_up(self):
        for i in self.buttons:
            i.destroy()
        self.buttons = []

    def refresh(self):
        self.clean_up()
        self.read_file(self.file_name)

    def show_message(self, text):
        messagebox.showinfo(message = text)


# second window frame Home
class Home(BaseFrame):

    def __init__(self, parent, controller):
        self.file_name = "Home Devices.txt"
        self.label_text = "Home Devices"
        super().__init__(parent, controller)

        
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Simple phrases",
                            command = lambda : controller.show_frame(Phrases))
     
        # putting the button in its place 
        # by using grid
        button1.grid(row = 3, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Home page",
                            command = lambda : controller.show_frame(HomePage))
     
        # putting the button in its place by 
        # using grid
        button2.grid(row = 3, column = 2, padx = 10, pady = 10)
                
# third window frame Phrases
class Phrases(BaseFrame): 
    
    def __init__(self, parent, controller):
        self.file_name = "Simple Phrases.txt"
        self.label_text = "Simple Phrases"
        super().__init__(parent, controller)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Home devices",
                            command = lambda : controller.show_frame(Home))
     
        # putting the button in its place by 
        # using grid
        button1.grid(row = 3, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Home Page",
                            command = lambda : controller.show_frame(HomePage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 3, column = 2, padx = 10, pady = 10)
  
def main():
    app = TalkBox()
    app.mainloop()

if __name__ == "__main__":
    main()