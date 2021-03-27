# This is prototype 2 for Talkbox

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter import PhotoImage
import tkinter.font as tkFont
 
LARGEFONT = ("Verdana", 15)


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
        tk.Frame.__init__(self, parent)
        photo1 = PhotoImage(file = "HomeDevicesPic.gif")
        photo1 = photo1.subsample(3,3)
        Style = tkFont.Font(family = "Verdana", size = 15)
        button1 = ttk.Button(self, text ="Talk to devices", image = photo1, compound = BOTTOM,
        command = lambda : controller.show_frame(Home))
        #button1.config(font = Style)
        button1.image = photo1
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        photo2 = PhotoImage(file = "SimplePhrasesPic.gif")
        photo2 = photo2.subsample(3,3)
        button2 = ttk.Button(self, text ="Talk to people", image = photo2, compound = BOTTOM,
        command = lambda : controller.show_frame(Phrases))
        button2.image = photo2
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 1, column = 5, padx = 10, pady = 10)

    def refresh(self):
        pass
  
class BaseFrame(tk.Frame):
    
    global buttonL
    global curBut
    global varRow
    global varColumn
    curBut = [-1,-1]
    buttonL = [[]]
    varRow = 1
    varColumn = 0
    

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text = self.label_text,)
        label.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.buttons = []


    def read_file(self, file_name):
        with open(file_name) as f:
            data = {i: line.strip() for i,line in enumerate(f, 1)}
        '''global buttonL 
        buttonL = [[]] 
        global curBut
        curBut = [-1,-1] 
        global varRow
        varRow = 1
        global varColumn
        varColumn = 0'''
        global h
        h = Scrollbar(orient = 'horizontal')
        h.pack(side = BOTTOM, fill = X)
        
        # buttons
        for i, name in data.items():
            button = ttk.Button(self, text = name)
                                #command = lambda name = name: self.show_message(name))
            
            buttonL[varRow-1].append(button)
            button.grid(row = varRow, column = varColumn, padx = 10, pady = 10)
            

            button.bind("<Left>", self.left)
            button.bind("<Right>", self.right)
            button.bind("<Down>", self.down)
            button.bind("<Up>", self.up)
            varColumn +=1

            #x = varRow - 1
            #y = varRow
            #z = varColumn
            #buttonL[x].append(button)
            #button.grid(row = y, column = z, padx = 10, pady = 10)
            #self.buttons.append(button)
            #z += 1
            '''if z > 10:
                z = 0
                y += 1
                buttonL.append([])

        tk.Frame.bind('<Left>', self.leftKey('<Left>'))
        tk.Frame.bind('<Right>', self.rightKey('<Right>'))
        tk.Frame.bind('<Up>', self.upKey('<Up>'))
        tk.Frame.bind('<Down>', self.downKey('<Down>'))'''

    def left(self, event):
        #messagebox.showinfo(message = "left")
        if curBut == [-1,-1]:
            curBut[:] = [0,0]
            buttonL[0][0].configure(highlightthickness = 10, highlightbackground = 'black')
    
    def right(self, event):
        messagebox.showinfo(message = "right")

    def up(self, event):
        messagebox.showinfo(message = "up")

    def down(self, event):
        messagebox.showinfo(message = "down")


    def clean_up(self):
        for i in self.buttons:
            i.destroy()
        self.buttons = []

    def refresh(self):
        self.clean_up()
        self.read_file(self.file_name)

    def show_message(self, text):
        messagebox.showinfo(message = text)

    def speak_out_loud(self, text):
        '''espeak stuff
        '''
    
    def leftKey(self, event):
        if curBut == [-1,-1]:
            curBut[:] = [0,0]
            buttonL[0][0].configure(highlightbackground='red')
        elif curBut[0] == 4:
            buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
            curBut[:] = [0,10]
            buttonL[0][10].configure(highlightbackground='red')
        else:
            buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
            curBut[:] = [curBut[0], (curBut[1]-1)%11]
            buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
        buttonL[curBut[0]][curBut[1]].focus_set()

    def rightKey(self, event):
        if curBut == [-1,-1]:
            curBut[:] = [0,0]
            buttonL[0][0].configure(highlightbackground='red')
        elif curBut[0] == 4:
            buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
            curBut[:] = [0,0]
            buttonL[0][0].configure(highlightbackground='red')
        else:
            buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
            curBut[:] = [curBut[0], (curBut[1]+1)%11]
            buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
        buttonL[curBut[0]][curBut[1]].focus_set()

    def upKey(self, event):
        if curBut == [-1,-1]:
            curBut[:] = [0,0]
            buttonL[0][0].configure(highlightbackground='red')
        elif curBut[0] == 0:
            buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
            curBut[:] = [(curBut[0]-1)%5, 0]
            buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
        elif curBut[0] == 4:
            buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
            curBut[:] = [(curBut[0]-1)%5, 5]
            buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
        else:
            buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
            curBut[:] = [(curBut[0]-1)%5, curBut[1]]
            buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
        buttonL[curBut[0]][curBut[1]].focus_set()

    def downKey(self, event):
        if curBut == [-1,-1]:
            curBut[:] = [0,0]
            buttonL[0][0].configure(highlightbackground='red')
        elif curBut[0] == 3:
            buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
            curBut[:] = [(curBut[0]+1)%5, 0]
            buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground='red')
        elif curBut[0] == 4:
            buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
            curBut[:] = [(curBut[0]+1)%5, 5]
            buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground='red')
        else:
            buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
            curBut[:] = [(curBut[0]+1)%5, curBut[1]]
            buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
        buttonL[curBut[0]][curBut[1]].focus_set()
    


# second window frame Home
class Home(BaseFrame):

    def __init__(self, parent, controller):
        self.file_name = "Home Devices.txt"
        self.label_text = "Talk to devices"
        super().__init__(parent, controller)

        
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Talk to people",
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
        self.label_text = "Talk to people"
        super().__init__(parent, controller)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Talk to devices",
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