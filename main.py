from datetime import date, datetime

from datetime import datetime
from tkinter import *
import PyPDF2
from PIL import Image, ImageTk

root = Tk()
root.title("Glucometer App")
root.geometry("500x600")

myLabel = Label(root, text="Enter your sugar level in mmol/L: ")
myLabel.pack()

myTextBox = Entry(root)
myTextBox.pack()


def get_level():
    now = datetime.now()
    levelMol = float(myTextBox.get())
    levelMg = levelMol * 18
    level_label = Label(root, text="The sugar levels have been written in the newfile.txt")
    level_label.pack()
    dt_string = now.strftime("%d/%m/%Y \n%H:%M:%S")
    f = open("newfile.txt", "a")
    f.write(f"\n{dt_string}" + f"\t\t\t\t{levelMol}" + f"\t\t\t\t\t{levelMg.__round__(2)}")
    f.write("\n--------------------------------------------------------------")
    f.close()


myButton = Button(root, text="Submit", command=get_level)
myButton.pack()

root.mainloop()
