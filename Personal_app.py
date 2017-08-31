from tkinter import *
from tkinter import ttk




def menu():
    print("Welcome! \n 1. Calculator \n 2. Reminders \n 3. To-do List \n 4. Contacts Info")
    choice = input()

    if choice == "1":
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

                root.resizable(width=False, height=False)

                style = ttk.style()
                style.configure("Tbutton",
                                font="serif 13",
                                padding=10)
                self.number_entry = ttk.Entry(root,
                                              textvatiable=self.entry_value, width=50)

                self.number_entry.grid(row=0, columnspan=4)
                self.button7 = ttk.Button(root, text="7",
                                          command=lambda: self.button_press("7")).grid(row=1, column=0)
                self.button8 = ttk.Button(root, text="8",
                                          command=lambda: self.button_press("8")).grid(row=1, column=1)
                self.button9 = ttk.Button(root, text="9",
                                          command=lambda: self.button_press("9")).grid(row=1, column=2)
                self.button_div = ttk.Button(root, text="/",
                                             command=lambda: self.math_button_press("/")).grid(row=1, column=3)
                self.button_mult = ttk.Button(root, text="*",
                                              command=lambda: self.math_button_press("*")).grid(row=1, column=4)

        root = Tk()
        calc = Calculator(root)
        root.mainloop()


    if choice == "2":
        print ("")

    if choice == "3" :
        print("")

    if choice == "4" :\
        print("")
