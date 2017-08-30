from tkinter import *
from tkinter import ttk

class Calculator:
    calc_value = 0.0

    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False

    def __init__(self, root):
        self.entry_value = StringVar(root, value="")
        root.title("Calculator")

        root.geometry("400x400")  # probably wrong

        root. resizable(width=False, height=False)

        style = ttk.style()
        style.configure("Tbutton",
                        font="serif 13",
                        padding=10)
        self.number_entry = ttk.Entry(root,
                                      textvatiable=self.entry_value,width=50)

        self.number_entry,grid(row=0, columnspan=4)



def menu () :
    print("Welcome! \n 1. Calculator \n 2. Reminders \n 3. To-do List \n 4. Contacts Info")
    choice = input()

    if choice == "1" :
        print("")


    if choice == "2" :
        print ("")

    if choice == "3" :
        print("")
