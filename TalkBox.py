# This is prototype 2 for Talkbox

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter import PhotoImage
#import tkinter.font as tkFont
 


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
            #frame.pack(fill = BOTH, expand = 1)
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
        self.buttonList=[]
        self.last_state = 0
        tk.Frame.__init__(self, parent)
        photo1 = PhotoImage(file = "HomeDevicesPic.gif")
        photo1 = photo1.subsample(1,1)
        s = ttk.Style()
        s.configure('X.TButton', font = ('Times New Roman', 20))
        button1 = ttk.Button(self, text ="Talk to devices", style = 'X.TButton', image = photo1, compound = BOTTOM,
        command = lambda : controller.show_frame(Home))
        self.buttonList.append(button1)
        button1.focus()
        button1.image = photo1
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        photo2 = PhotoImage(file = "SimplePhrasesPic.gif")
        photo2 = photo2.subsample(1,1)
        button2 = ttk.Button(self, text ="Talk to people", style = 'X.TButton', image = photo2, compound = BOTTOM,
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
        tk.Frame.__init__(self, parent)
        #label = ttk.Label(self, text = self.label_text)
        #label.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.buttons = []
        self.curBut = [-1,-1]
        self.buttonL = [[]]
        self.varRow = 0
        self.make_nav_buttons(controller)

        self.current_column = 0
        self.last_state = 0
        self.current_row = 0

        # Create a canvas 
        self.my_canvas = Canvas(self)
        self.my_canvas.grid(row = 0, column = 1, sticky = 'news')

        # Create a scrollbar and set its command to scroll through the canvas
        self.h = tk.Scrollbar(self, orient = tk.HORIZONTAL, command = self.my_canvas.xview)
        self.h.grid(column = 1, sticky = 'ew')

        self.my_canvas.configure(xscrollcommand = self.h.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all")))

        # Create a 2nd frame to store buttons inside the the canvas
        self.frame_buttons = tk.Frame(self.my_canvas)
        self.my_canvas.create_window((0,0), window=self.frame_buttons, anchor='nw')

        
        
    def read_file(self, file_name):
        with open(file_name) as f:
            data = {i: line.strip() for i,line in enumerate(f, 1)}
        varColumn = 0
        
        for i, name in data.items():
            # Styling the button
            q = ttk.Style()
            q.configure('W.TButton', relief="flat", background = 'white', foreground = 'black', font = ('Times New Roman', 14))
            
            # Creating buttons from the data and placing them in the frame
            button = ttk.Button(self.frame_buttons, text = name, style = 'W.TButton',
                                command = lambda name = name: self.speak_out_loud(name))
            
            self.buttonL[self.varRow].insert(varColumn, button)
            button.grid(row = self.varRow, column = varColumn, padx = 10, pady = 10, ipadx = 10, ipady=10, sticky = 'news')
            self.buttons.append(button)

            # bind keyboard keys to each button
            self.bind_keys(button)

            # update the scroll region with the creation of each button
            self.updateScrollRegion()
            varColumn +=1

        if self.buttonL and self.buttonL[0]:
            self.buttonL[0][0].focus()
        
    def updateScrollRegion(self):
        self.my_canvas.update_idletasks()
        self.my_canvas.config(scrollregion = self.frame_buttons.bbox())
    

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
        self.current_column = 0
        self.current_row = 0
        button.bind("<Down>", lambda event : self.change(event, "vertical"))
        button.bind("<Return>", lambda event : event.widget.invoke())
        

    def make_nav_buttons(self, controller):
        b = self.nav_buttons = []
        # button to show frame 2 with text
        # layout2
        st = ttk.Style()
        st.configure('B.TButton', relief="flat", background = 'white', foreground = 'black', font = ('Times New Roman', 10))
        button = ttk.Button(self, text = self.other_label, style = 'B.TButton',
                            command = lambda : controller.show_frame(self.other_frame))
        b.append(button)
     
        # putting the button in its place 
        # by using grid
        self.bind_keys(button)
        button.grid(row = 3, column = 0, padx = 10, pady = 10, ipadx = 10, ipady=10)
  
        # button to show frame 2 with text
        # layout2
        button = ttk.Button(self, text = "Home page", style = 'B.TButton',
                            command = lambda : controller.show_frame(HomePage))
     
        # putting the button in its place by 
        # using grid
        self.bind_keys(button)
        
        button.grid(row = 3, column = 2, padx = 10, pady = 10, ipadx = 10, ipady=10)

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

            if (b == self.buttons) :
                frac1 = col/len(b)
                self.my_canvas.xview_moveto(frac1)

        elif direction == "right":
            if self.current_row == 0:
                b = self.buttons
            else:
                b = self.nav_buttons
      
            col = self.current_column = (self.current_column + 1) % len(b)
            b[col].focus()
        
            if b == self.buttons:
                frac1 = col/len(b)
                self.my_canvas.xview_moveto(frac1)

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
    app.geometry("620x420")
    app.mainloop()

if __name__ == "__main__":
    main()