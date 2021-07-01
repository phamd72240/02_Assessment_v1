from tkinter import *
from functools import partial  # To prevent unwanted windows
import random

class Start:
    def __init__(self, parent):

        # GUI to get starting question and level
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Mystery Heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="God quiz",
                                       font="Arial 19 bold")
        self.mystery_box_label.grid(row=1)

        # Play Button (row 2)
        self.lowlevel_button = Button(text="10 question",
                                       command=lambda: self.to_quiz(1))
        self.lowlevel_button.grid(row=2, pady=10)
        self.highlevel_button = Button(text="20 question",
                                       command=lambda: self.to_quiz(1))
        self.highlevel_button.grid(row=3, pady=10)
        self.midlevel_button = Button(text="30 question",
                                       command=lambda: self.to_quiz(1))
        self.midlevel_button.grid(row=4, pady=10)


class quiz:
    def __init__(self, partner, level, starting_question):
        print(level)
        print(starting_question)

        # disable low level button
        partner.lowlevel_button.config(state=DISABLED)

        # initialise variables
        self.question = IntVar()

        # set starting question to amount entered by user at start of quiz
        self.question.set(starting_question)

        # GUI Setup
        self.quiz_box = Toplevel()
        self.quiz_frame = Frame(self.quiz_box)
        self.quiz_frame.grid()

        # Heading Row
        self.heading_label = Label(self.quiz_frame, text="Heading",
                                   font="Arial 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)



# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Start(root)
    root.mainloop()
