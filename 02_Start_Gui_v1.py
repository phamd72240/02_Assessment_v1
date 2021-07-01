from tkinter import *
import random


class Start:
    def __init__(self, partner):
        # Start GUI
        self.start_frame = Frame(padx=10, pady=10, bg="#D4E1F5")
        self.start_frame.grid()

        # background
        background = "#D4E1F5"

        # Mystery box Heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="Egyptian God Quiz",
                                       font="Arial 16 bold", bg=background)
        self.mystery_box_label.grid(row=0)

        # Initial instructions (row 1)
        self.mystery_instructions = Label(self.start_frame, text=" Please choose the amount of "
                                                                 "question you want to answer",
                                          font="Arial 8 italic", fg="black", bg=background)
        self.mystery_instructions.grid(row=1)

        # Buttons frame ( row 3)

        self.level_frame = Frame(self.start_frame, bg=background)
        self.level_frame.grid(row=3)

        # Button Font
        button_font = "Oswald 12 bold"

        # Low Questions Button
        self.low_level_button = Button(self.level_frame, text="10",
                                        font=button_font, bg="#FF9933",
                                        command=lambda: self.to_quiz(1))
        self.low_level_button.grid(row=0, column=0, pady=10, padx=5)

        # Medium Questions Button
        self.med_level_button = Button(self.level_frame, text="20",
                                        font=button_font, bg="#FFFF33",
                                        command=lambda: self.to_quiz(2))
        self.med_level_button.grid(row=0, column=1, pady=10, padx=5)

        # High Questions Button
        self.high_level_button = Button(self.level_frame, text="30",
                                         font=button_font, bg="#09FF33",
                                         command=lambda: self.to_quiz(3))
        self.high_level_button.grid(row=0, column=2, pady=10, padx=5)

        # Button frame for help and statistics (row 5)
        self.start_help_frame = Frame(self.start_frame, bg="#D4E1F5")
        self.start_help_frame.grid(row=5)

        # Help and statistics buttons
        self.start_help_button = Button(self.start_help_frame, text="Instructions",
                                        font="Arial 10 bold", bg="#E6E6E6",
                                        command=lambda: self.to_help)
        self.start_help_button.grid(row=0, column=0)

class quiz:
    def __init__(self, partner, level,):
        print(level)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Start(root)
    root.mainloop()