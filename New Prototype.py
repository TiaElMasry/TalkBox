# This is prototype 2 for Talkbox

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
 
LARGEFONT =("Verdana", 35)
  
class TalkBox(tk.Tk):
     
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
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
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(HomePage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    
 
# first window frame HomePage
  
class HomePage(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        photo = PhotoImage(file = "HomeDevicesPic.png")
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
  
          
  
  
# second window frame Home
class Home(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Home devices",)
        label.grid(row = 0, column = 2, padx = 10, pady = 10)

        
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

        # reading home devices file
        f = open("Home Devices.txt").readlines()
        my_dict = {}

        # creating a dictionary of all options and a list of
        list1 = []
        list2 = []
        for i in range(len(f)):
            t = f[i]
            my_dict[i+1] = t
            list1.append(t)
            list2.append(i+1)

        # buttons
        for i in range(len(my_dict)):
            name = my_dict[i+1]
            button = ttk.Button(self, text = name,
                                command = lambda name = name: self.show_message(name))
            button.grid(row = 2, column = i+1, padx = 10, pady = 10)


    def show_message(self, text):
        messagebox.showinfo(message = text)

                
# third window frame Phrases
class Phrases(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Simple Phrases")
        label.grid(row = 0, column = 2, padx = 10, pady =10)
  
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
  

        # reading simple phrases file
        f = open("Simple Phrases.txt").readlines()
        my_dict = {}

        # creating a dictionary of all options
        for i in range(len(f)):
            t = f[i]
            my_dict[i+1] = t

        # buttons
        for i in range(len(my_dict)):
            name = my_dict[i+1]
            button = ttk.Button(self, text = my_dict[i+1],
                                command = lambda name = name: self.show_message(name))
            button.grid(row = 2, column = i+1, padx = 10, pady = 10)

    def show_message(self, text):
        messagebox.showinfo(message = text)

# Driver Code
app = TalkBox()
app.mainloop()
