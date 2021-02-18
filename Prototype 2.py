# This is prototype 2 for Talkbox

import tkinter as tk
    

def home_devices():
    f = open("Home Devices.txt").readlines()
    my_dict = {}
    
    for i in range(len(f)):
        t = f[i]
        my_dict[i+1] = t
    print(my_dict)
    return my_dict

def simple_phrases():
    f = open("Simple Phrases.txt").readlines()
    my_dict = {}
    
    for i in range(len(f)):
        t = f[i]
        my_dict[i+1] = t
    print(my_dict)
    return my_dict


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
