import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror



class Category1ConverterFrame(ttk.Frame):

    def __init__(self, container, unit_from, converter):
        super().__init__(container)

        # field options
        options = {'padx': 5, 'pady': 1}

        self.frame = ttk.Frame(self)
        self.l = ttk.Label(self.frame, text="类别1")
        self.l.pack()
        self.frame.grid(column=0, row=0, sticky='w', **options)

        # add padding to the frame and show it
        self.grid(column=0, row=1, sticky="nsew", **options)


    def reset(self):
        pass

