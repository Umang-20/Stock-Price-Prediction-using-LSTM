# Import module
from tkinter import *
from PIL import ImageTk, Image

# Create object
root = Tk()

# Adjust size
root.geometry("600x500")

# Title
root.title("Stock Price Prediction")


# function
def graph():
    if clicked.get() == "Nifty 50":
        load = Image.open("Predicted Graph/NSE_Predicted_Graph.png")
        load = load.resize((576, 288))
        render = ImageTk.PhotoImage(load)
        img = Label(root, image=render)
        img.image = render
        img.grid(row=3, column=0, columnspan=10, padx=10)

    if clicked.get() == "Sensex":
        load = Image.open("Predicted Graph/Sensex_Predicted_Graph.png")
        load = load.resize((576, 288))
        render = ImageTk.PhotoImage(load)
        img = Label(root, image=render)
        img.image = render
        img.grid(row=3, column=0, columnspan=10, padx=10)

    if clicked.get() == "Reliance":
        load = Image.open("Predicted Graph/Reliance_Predicted_Graph.png")
        load = load.resize((576, 288))
        render = ImageTk.PhotoImage(load)
        img = Label(root, image=render)
        img.image = render
        img.grid(row=3, column=0, columnspan=10, padx=10)

    if clicked.get() == "TCS":
        load = Image.open("Predicted Graph/TCS_Predicted_Graph.png")
        load = load.resize((576, 288))
        render = ImageTk.PhotoImage(load)
        img = Label(root, image=render)
        img.image = render
        img.grid(row=3, column=0, columnspan=10, padx=10)

    if clicked.get() == "Infosys":
        load = Image.open("Predicted Graph/Infosys_Predicted_Graph.png")
        load = load.resize((576, 288))
        render = ImageTk.PhotoImage(load)
        img = Label(root, image=render)
        img.image = render
        img.grid(row=3, column=0, columnspan=10, padx=10)


def clear():
    img.config(text="")


# Dropdown menu options
options = [
    "Nifty 50",
    "Sensex",
    "Reliance",
    "TCS",
    "Infosys"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Nifty 50")

# Create Label
label = Label(root, text="Select the Stock:")
label.grid(row=0, column=0, pady=20, columnspan=2)

img = Label(root)
# Create Dropdown menu
drop = OptionMenu(root, clicked, *options)
drop.grid(row=0, column=2, pady=20)

# Create button, it will change label text
button = Button(root, text="Click Me", command=graph).grid(row=1, column=0, pady=20, columnspan=2)
clear = Button(root, text="Clear", command=clear).grid(row=1, column=2, pady=20)

# Execute tkinter
root.mainloop()
