import tkinter as tk
from tkinter import ttk

from src.utils.temperatureConverter import TemperatureConverter
from src.gui.converterFrame.category2ConverterFrame import Category2ConverterFrame
from src.gui.converterFrame.category1ConverterFrame import Category1ConverterFrame


class ControlFrame(ttk.LabelFrame):

    def __init__(self, container):
        super(ControlFrame, self).__init__(container)

        self['text'] = '类型'
        options = {'padx': 0, 'pady': 1}
        # radio buttons
        self.selected_value = tk.IntVar()
        ttk.Radiobutton(
            self,
            text='类别1',
            value=0,
            variable=self.selected_value,
            command=self.change_frame).grid(column=0, row=0, **options)

        ttk.Radiobutton(
            self,
            text='类别2',
            value=1,
            variable=self.selected_value,
            command=self.change_frame).grid(column=1, row=0, **options)


        self.grid(column=0, row=0, sticky='w', **options)

        # initialize frames
        self.frames = {}
        self.frames[0] = Category1ConverterFrame(
            container,
            '类别1',
            TemperatureConverter.celsius_to_fahrenheit)
        self.frames[1] = Category2ConverterFrame(
            container,
            '类别2',
            TemperatureConverter.celsius_to_fahrenheit)

        self.change_frame()

    def change_frame(self):
        self.frame = self.frames[self.selected_value.get()]
        self.frame.reset()
        self.frame.tkraise()
