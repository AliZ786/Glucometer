from datetime import datetime
from tkinter import *
import tkinter.font as tkFont
import os
from PIL import ImageTk, Image
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

# Initialisation of the GUI window
root = Tk()
root.title("Glucometer App")
root.geometry("500x600")

# Add title to the GUI window
title = Label(root, text="Glucometer App")
titleFont = tkFont.Font(family='Times New Roman', size=30,
                        weight="bold", slant="italic", underline=True)
title.configure(font=titleFont, fg="black")
title.pack()
nameLabel = Label(root, text="\nEnter your name")
nameLabel.pack()
nameBox = Entry(root)
nameBox.pack()

# Current time display on the text-file and name box
def get_name():
    
    name_get = nameBox.get()
    return name_get
    


myLabel = Label(root, text="\nEnter your sugar level in mmol/L: ")
myFont = tkFont.Font(family="Times New Roman", size=14, weight="bold")
myLabel.configure(font=myFont)
myLabel.configure(fg="blue")
myLabel.pack()
input = Entry(root)
input.pack()

def get_level():
    get_name()
    in_Mols = input.get()
    in_Mg = (float(in_Mols))*18
    print(in_Mg)

    f = open("file1.txt", "a")
    f.write("------------ " + f"{nameBox.get()}" + " sugar level's file ---------")
    f.write(in_Mols)
    f.write(str(in_Mg))





myButton = Button(root, text="Submit", command= get_level, bg="red", fg="white")
myButton.pack()

root.mainloop()
