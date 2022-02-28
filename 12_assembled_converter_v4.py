from tkinter import *
from functools import partial
import os
import re
from datetime import datetime
from turtle import back
from PIL import ImageTk,Image


class Converter:
    def __init__(self, parent):
        
        # Formatting Variables...
        background_color = "light blue"

        # Initialise list hold calculation history
        self.all_calc_list = []

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=600, height=600, bg=background_color, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (Row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter", font=("Arial", "16", "bold"), bg=background_color, padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        self.canvas = Canvas(self.converter_frame, width = 300, height = 300, bg=background_color)
        self.canvas.grid(row=1)
        self.img = ImageTk.PhotoImage(Image.open("icon.png"))     
        self.canvas.create_image(0,0,anchor=NW, image=self.img)    
        
        # User Instructions (Row 1)
        self.temp_instructions_label = Label(self.converter_frame, text="Type in the amount to be converted and then push one of the buttons below...", font="Arial 10 italic", wrap=290, justify=LEFT, bg=background_color, padx=10, pady=10)
        self.temp_instructions_label.grid(row=2)

        # Temperature Entry Box (Row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20, font="Arial 14 bold")
        self.to_convert_entry.grid(row=3)

        # Conversion Buttons Frame (Row 3)
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=4, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame, text="To Centigrade", font="Arial 10 bold", bg = "Khaki1", padx=10, pady=10, command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame, text="To Fahrenheit", font="Arial 10 bold", bg="Orchid1", padx=10, pady=10, command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)
        
        #Answer Label (Row 4)
        self.answer_label = Label(self.converter_frame, text="Conversion will appear here...", font="Arial 10 bold", wrap=250, bg=background_color, padx=10, pady=10)
        self.answer_label.grid(row=5)

        # Hist/Help Frame (Row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=6, pady=10)

        # History Button (Hist/Help Frame, Row 0)
        self.history_button = Button(self.hist_help_frame, text="History", font=("Arial", "14"), padx=10, pady=10, command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=0, column=0)

        # Help Button (Hist/Help Frame, Row 0)
        self.help_button = Button(self.hist_help_frame, text="Help", font=("Arial", "14"), padx=10, pady=10, command=self.help)
        self.help_button.grid(row=0, column=1)

        if len(self.all_calc_list) == 0:
            self.history_button.config(state=DISABLED)

    def temp_convert(self, low):
        print(low)

        error = "#ffafaf" # Pale Pink

        # Retrieve amount entered into entry field
        to_convert = self.to_convert_entry.get()

        # Check amount is a valid number
        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # Check and convert to F
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert, fahrenheit)

            # Check and convert to C
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degrees F is {} degrees C".format(to_convert, celsius)

            else:
                answer = "Too cold!"
                has_errors == "no"

            # Display Answer
            if has_errors == "no":
                self.answer_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            else:
                self.answer_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)

            # Add Answer to list for history
            if answer != "Too cold!":
                self.all_calc_list.append(answer)
                self.history_button.config(state=NORMAL)

        except ValueError:
            self.answer_label.configure(text="Enter a number!!", fg="red")
            self.to_convert_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)
        
        return rounded

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Please enter a number in the box and then push one of the buttons to convert then number to either degrees C or degrees F.\n\nThe Calculation History area shows up to seven past calculations (most recent at the top).\n\nYou can also export your full calculation history to a text file if desired")

    def history(self, calc_history):
        History(self, calc_history)

class Help:
    def __init__(self, partner):

        background = "orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()
        
        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Set up Help heading (Row 0)
        self.how_heading = Label(self.help_frame, text="Help/Instructions", font=("Arial", "14", "bold"), bg=background)
        self.how_heading.grid(row=0)

        # Help text (Label, Row 1)
        self.help_text = Label(self.help_frame, text="This is Help", justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (Row 2)
        self.dismiss_button = Button(self.help_frame, text="Dismiss", width=10, bg=background, font=("Arial", "10", "bold"), command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, pady=10)

    def close_help(self,partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

class History:
    def __init__(self, partner, calc_history):

        background = "#a9ef99" # Pale green

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (ie: history box)
        self.history_box = Toplevel()
        
        # If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        # Set up history heading (Row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History", font=("Arial", "19", "bold"), bg=background)
        self.how_heading.grid(row=0)

        # History text (Label, Row 1)
        self.history_text = Label(self.history_frame, text="Here are your most recent calculations. Please use the export button to create a text file of all your calculations for this session", font="arial 10 italic", justify=LEFT, width=40, fg="maroon", bg=background, wrap=250, padx=10, pady=10)
        self.history_text.grid(row=1)

        # History Output (Row 2)
        # Generate string from list of calculations
        history_string = ""

        if len(calc_history) >= 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history) - item - 1]+"\n"
        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) - calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here is your calculation history. You can use the export button to save this data to text file if desired.")

        # Label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string, bg=background, font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # Export / Dismiss Buttons Frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export button
        self.export_button = Button(self.export_dismiss_frame, text="Export", font=("Arial", "12", "bold"), command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        # Dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss", font=("Arial", "12", "bold"), command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self,partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, calc_history):
        Export(self, calc_history)

class Export:
    def __init__(self, partner, calc_history):

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
        self.how_heading = Label(self.export_frame, text="Export / Instructions", font=("Arial", "14", "bold"), bg=background)
        self.how_heading.grid(row=0)

        # Export instructions (Label, Row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename in the box below and press the Save button to save your calculation history to a text file.", justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (Label, Row 2)
        self.export_text = Label(self.export_frame, text="If the filename you enter below already exists its contents will be replaced with your calculation history", justify=LEFT, width=40, bg="#ffafaf", fg="maroon", wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20, font="Ariel 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon", bg=background)
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel Buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save", command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel", command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, calc_history):
        
        # Regular Expression to check filename is valid
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = "(no {}'s allowed)".format(letter)
            has_error = "yes"
            break

        if filename == "":
            problem = "Can't be blank"
            has_error = "yes"
        
        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            # If there are no errors, generate text file and then close dialogue
            # Add .txt suffix
            filename = filename + ".txt"

            # Create file to hold data
            f = open(filename, "w+") # Press to pay respects

            # Writes a title in the file
            f.write("CALCULATION HISTORY:\n\n")

            # Writes the date on when the calculations were made
            now = datetime.now()

            current_time = now.strftime("%H:%M")
            current_date = now.strftime("%D")
            f.write("Date: {}   |   Time: {}\n\n".format(current_date, current_time))

            # Add new line at the end of each item
            for item in calc_history:
                f.write(item + "\n")

            # Close file
            f.close()

            # Close dialogue
            self.close_export(partner)

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
