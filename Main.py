from tkinter import *

class Calculator:

    def __init__(self, master):

        self.master = master


        master.title("Python Calculator")

        self.equation=Entry(master, width=36, borderwidth=5)
        self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.createButton()
        
        def createButton(self):

        b0 = self.addButton(0)
        b1 = self.addButton(1)
        b2 = self.addButton(2)
        b3 = self.addButton(3)
        b4 = self.addButton(4)
        b5 = self.addButton(5)
        b6 = self.addButton(6)
        b7 = self.addButton(7)
        b8 = self.addButton(8)
        b9 =  self.addButton(9)
        b_add = self.addButton('+')
        b_sub = self.addButton('-')
        b_mult = self.addButton('*')
        b_div = self.addButton('/')
        b_clear = self.addButton('c')
        b_equal = self.addButton('=')

