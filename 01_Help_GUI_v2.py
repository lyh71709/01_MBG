from tkinter import *
import random
import os


class Converter:
    def __init__(self, parent):
        
        # Formatting Variables...
        background_color = "light blue"

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=600, height=600, bg=background_color, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (Row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter", font=("Ariel", "16", "bold"), bg=background_color, padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # Help Button (Row 1)
        self.help_button = Button(self.converter_frame, text="Help", font=("Ariel", "14"), padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

class Help:
    def __init__(self, partner):

        background = "orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()
        
        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Set up Help heading (Row 0)
        self.how_heading = Label(self.help_frame, text="Help/Instructions", font=("Ariel", "14", "bold"), bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, Row 1)
        self.help_text = Text(self.help_frame, text="Hello this is help", justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(column=1, row=1)

        # Dismiss button (Row 2)
        self.dismiss_button = Button(self.help_frame, text="Dismiss", width=10, bg=background, font=("Ariel", "10", "bold"), command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, pady=10)

    def close_help(self,partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

# main routine
clear = lambda:os.system('cls')
clear()

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()

()