# This is prototype 2 for Talkbox

import tkinter as tk
from tkinter import messagebox
    
# Creates a home devices dictionary
def home_devices():
    f = open("Home Devices.txt").readlines()
    my_dict = {}
    
    for i in range(len(f)):
        t = f[i]
        my_dict[i+1] = t
    make_buttons(my_dict)
    return my_dict

# Creates a simple phrases dictionary
def simple_phrases():
    f = open("Simple Phrases.txt").readlines()
    my_dict = {}
    
    for i in range(len(f)):
        t = f[i]
        my_dict[i+1] = t
    make_buttons(my_dict)
    return my_dict

#Print the message that corresponds to the specific int input in that specified dictionary
def print_text(x, my_dict):
    print(my_dict[x])
    messagebox.showinfo(message = my_dict[x])
    
    
    
# Takes dictionary as input and creates a set of buttons
def make_buttons(x):
    for i in range(len(x)):
        name1 = tk.Button(
            frame,
            text= x[i+1])
        name1.pack(side=tk.LEFT)


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

home = tk.Button(
    frame,
    text="Home Devices",
    command=home_devices)

home.pack(side=tk.LEFT)

phrases = tk.Button(frame,
    text="Simple Phrases",
    command=simple_phrases)

phrases.pack(side=tk.LEFT)

root.mainloop()

