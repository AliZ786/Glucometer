from datetime import datetime
from tkinter import *
import tkinter.font as tkFont
import os
from PIL import ImageTk, Image
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

#Initialisation of the GUI window
root = Tk()
root.title("Glucometer App")
root.geometry("500x600")

title = Label(root, text= "Glucometer App")
titleFont = tkFont.Font(family='Times New Roman', size=30, weight="bold", slant="italic", underline=True)
title.configure(font=titleFont, fg="black")
title.pack()

root.mainloop()
