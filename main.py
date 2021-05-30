from datetime import datetime
from tkinter import *
import tkinter.font as tkFont
import os
from PIL import ImageTk, Image

root = Tk()
root.title("Glucometer App")

root.geometry("500x600")


myTitle = Label(root, text="Glucometer app")
myTitleFont = tkFont.Font(family="Times New Roman", size=30, weight="bold")
myTitle.configure(font=myTitleFont, fg="gray")
myTitle.pack()

myLabel = Label(root, text="\nEnter your sugar level in mmol/L: ")
myFont = tkFont.Font(family="Times New Roman", size=14, weight="bold")
myLabel.configure(font=myFont)
myLabel.configure(fg="blue")
myLabel.pack()

myTextBox = Entry(root)
myTextBox.pack()

fileName = "sugarlevels.txt"


def get_level():
    now = datetime.now()
    levelMol = float(myTextBox.get())
    levelMg = levelMol * 18
    level_label = Label(root, text=f"The sugar levels have been written in {fileName}")
    level_label.configure(font=myFont, fg="green")
    level_label.pack()
    dt_string = now.strftime("%d/%m/%Y \n%H:%M:%S")

    f = open(fileName, "a")
    if os.stat(fileName).st_size == 0:
        f.write("Date/Time" + "\t\t Sugar level(mmol/L)" + "\t\t Sugar level(mg/dL)")
        f.write("\n--------------------------------------------------------------")
        f.write(f"\n{dt_string}" + f"\t\t\t\t{levelMol}" + f"\t\t\t\t\t{levelMg.__round__(2)}")

    else:
        f.write(f"\n{dt_string}" + f"\t\t\t\t{levelMol}" + f"\t\t\t\t\t{levelMg.__round__(2)}")
    f.write("\n--------------------------------------------------------------")
    f.close()


myButton = Button(root, text="Submit", command=get_level, bg="red", fg="white")
myButton.pack()

root.mainloop()
