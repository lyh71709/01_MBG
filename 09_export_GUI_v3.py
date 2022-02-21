from tkinter import *
import random 
from functools import partial
import os


class Converter:
    def __init__(self, parent):
        
        # Formatting Variables...
        background_color = "light blue"

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=600, height=600, bg=background_color, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (Row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter", font=("Arial", "16", "bold"), bg=background_color, padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # Export Button (Row 1)
        self.export_button = Button(self.converter_frame, text="Export", font=("Arial", "14"), padx=10, pady=10, command=self.export)
        self.export_button.grid(row=1)

    def export(self):
        print("You asked for export")
        get_export = Export(self)
        get_export.export_text.configure(text="Export text goes here")

class Export:
    def __init__(self, partner):

        background = "orange"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()
        
        # If users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, bg=background)
        self.export_frame.grid()

        # Set up Export heading (Row 0)
        self.how_heading = Label(self.export_frame, text="Export/Instructions", font=("Arial", "14", "bold"), bg=background)
        self.how_heading.grid(row=0)

        # Export instructions (Label, Row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename in the box below and press the Save button to save your calculation history to a text file.", justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (Label, Row 2)
        self.export_text = Label(self.export_frame, text="If the filename you enter below already exists iots contents will be replaced with your calculation history", justify=LEFT, width=40, bg="#ffafaf", fg="maroon", wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2)

        # Dismiss button (Row 3)
        self.dismiss_button = Button(self.export_frame, text="Dismiss", width=10, bg=background, font=("Arial", "10", "bold"), command=partial(self.close_export, partner))
        self.dismiss_button.grid(row=2, pady=10)

    def close_export(self,partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

# main routine
clear = lambda:os.system('cls')
clear()

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
