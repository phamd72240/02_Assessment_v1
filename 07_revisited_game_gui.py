from tkinter import *
from functools import partial # Prevent unwanted windows
import csv
import random


class Start:
    def __init__(self, partner,):
        # Start GUI
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        heading_label = Label(self.start_frame, text="Egyptian Gods Quiz", font="Arial 15 bold")
        heading_label.grid(row=0)

        egyptian_god_label = Label(self.start_frame, text="Question will go here, "
                                                      "some of them are quite long",
                               font="Arial 15 bold", justify=LEFT)
        egyptian_god_label.grid(row=1)

        self.answer_frame = Frame(self.start_frame)
        self.answer_frame.grid(row=2)

        # Top level button
        self.top_left_button = Button(self.answer_frame, text="Top left",
                                      font="Arial 15", width=15, height=1, bg="black", fg="yellow")
        self.top_left_button.grid(row=0, column=0, padx=5, pady=5)

        self.top_right_button = Button(self.answer_frame, text="Top right",
                                       font="Arial 15", width=15, height=1, bg="black", fg="yellow")
        self.top_right_button.grid(row=0, column=1)

        # Bottom level button
        self.bottom_left_button = Button(self.answer_frame, text="Bottom left",
                                         font="Arial 15", width=15, height=1, bg="black", fg="yellow")
        self.bottom_left_button.grid(row=1, column=0)

        self.bottom_right_button = Button(self.answer_frame, text="Bottom right",
                                          font="Arial 15", width=15, height=1, bg="black", fg="yellow")
        self.bottom_right_button.grid(row=1, column=1)

        # Label for results
        self.result_label = Label(self.start_frame, fg="black", font="Arial 14 bold",
                                  text="{} correct / {} games played")
        self.result_label.grid(row=3, column=0)

        # Next Button
        self.next_button = Button(self.start_frame, width=29, font="Arial 16 bold", height=1,
                                  text="Next", pady=5,
                                  background="black", fg="yellow")
        self.next_button.grid(row=4, column=0)

        # stats frame
        self.help_stats_frame = Frame(self.start_frame)
        self.help_stats_frame.grid(row=5)

        # Help Button
        self.start_help_button = Button(self.help_stats_frame, text="Help/Rules",
                                        font="Arial 15 bold", width=15,
                                        bg="black", fg="white")
        self.start_help_button.grid(row=0, column=0, padx=4, pady=10)

        # Stats Button
        self.statistics_button = Button(self.help_stats_frame, text="Stats / Export", width=15,
                                              font="Arial 15 bold", bg="black", fg="white",)
        self.statistics_button.grid(row=0, column=1)

        # Quit Button
        self.quit_button = Button(self.start_frame, text="Quit", fg="red", bg="white",
                                  font="Arial 12 bold", width=38, height=1)
        self.quit_button.grid(row=7)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Egyptian God Quiz")
    something = Start(root)
    root.mainloop()
