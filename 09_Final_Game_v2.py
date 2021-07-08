from tkinter import *
from functools import partial  # Prevent unwanted windows
import csv
import re
import random


class Start:
    def __init__(self, partner, ):
        # Start GUI
        self.start_frame = Frame(padx=10, pady=10, bg="#D4E1F5")
        self.start_frame.grid()

        # background
        background = "#D4E1F5"

        # God Quiz Heading (row 0)
        self.egyptian_god_label = Label(self.start_frame, text="Egyptian Gods Quiz",
                                        font="Arial 15 bold", bg="#D4E1F5")
        self.egyptian_god_label.grid(row=0)

        # Initial instructions (row 1)
        self.god_instructions_label = Label(self.start_frame, text=" Please choose the amount of "
                                                                   "question you want to answer",
                                            font="Arial 12 italic", fg="black", bg=background)
        self.god_instructions_label.grid(row=1)

        # to_quiz button frame
        self.to_quiz_frame = Frame(self.start_frame, bg=background)
        self.to_quiz_frame.grid(row=2)

        # to_stat button frame
        self.to_stat_frame = Frame(self.start_frame, bg=background)
        self.to_stat_frame.grid(row=2)

        # Buttons frame ( row 3)
        self.level_frame = Frame(self.start_frame, bg=background)
        self.level_frame.grid(row=3)

        # Button Font
        button_font = "Oswald 40 bold"

        # Low Questions Button
        self.low_level_button = Button(self.level_frame, text="10",
                                       font=button_font, bg="#FF9933",
                                       command=lambda: self.to_quiz(1))
        self.low_level_button.grid(row=5, column=0, pady=10, padx=5)

        # Medium Questions Button
        self.med_level_button = Button(self.level_frame, text="20",
                                       font=button_font, bg="#FFFF33",
                                       command=lambda: self.to_quiz(2))
        self.med_level_button.grid(row=5, column=1, pady=10, padx=5)

        # High Questions Button
        self.high_level_button = Button(self.level_frame, text="30",
                                        font=button_font, bg="#09FF33",
                                        command=lambda: self.to_quiz(3))
        self.high_level_button.grid(row=5, column=2, pady=10, padx=5)

        # Button frame for help and statistics (row 5)
        self.start_help_frame = Frame(self.start_frame, bg="#D4E1F5")
        self.start_help_frame.grid(row=5)

        # To quiz button

    def to_quiz(self, level):
        Game(self, level)

class Game:
    def __init__(self, partner, level):
        print(level)

        # Import the csv file, name of csv file goes here
        with open('Egyptian_gods.csv', 'r') as f:
            # make csv file into list
            file = csv.reader(f)
            next(f)
            my_list = list(file)

        # result
        self.result = 0

        # Amounts of game
        self.rounds_played = 0

        # Define said answer
        self.top_left = ""
        self.top_right = ""
        self.bottom_right = ""
        self.bottom_left = ""

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Label for the quiz
        self.egyptian_god_label = Label(self.game_frame, text="Egyptian Gods Quiz",
                                        font="Arial 15")
        self.egyptian_god_label.grid(row=0)

        # Label showing answer
        self.answer_label = Label(self.game_frame, text="Egyptian Gods Quiz", font="Arial 15")
        self.answer_label.grid(row=1)

        # Setup grid for answer buttons row 3
        self.answers_frame = Frame(self.game_box)
        self.answers_frame.grid(row=3)

        # Top level button
        self.top_left_button = Button(self.answers_frame, text="",
                                      font="Arial 15", width=35, bg="black", fg="yellow",
                                      command=lambda: self.reveal_answer(self.top_left))
        self.top_left_button.grid(column=0, row=0, padx=5, pady=5)

        self.top_right_button = Button(self.answers_frame, text="",
                                       font="Arial 15", width=35, bg="black", fg="yellow",
                                       command=lambda: self.reveal_answer(self.top_right))
        self.top_right_button.grid(column=1, row=0)

        # Bottom level button
        self.bottom_left_button = Button(self.answers_frame, text="",
                                         font="Arial 15", width=35, bg="black", fg="yellow",
                                         command=lambda: self.reveal_answer(self.bottom_left))
        self.bottom_left_button.grid(column=0, row=1)

        self.bottom_right_button = Button(self.answers_frame, text="",
                                          font="Arial 15", width=35, bg="black", fg="yellow",
                                          command=lambda: self.reveal_answer(self.bottom_right))
        self.bottom_right_button.grid(column=1, row=1)

        # Label for results
        self.result_label = Label(self.game_box, font="Arial 14 bold", fg="black",
                                  text="{} correct / {} games played".format(self.result,
                                                                             self.rounds_played))
        self.result_label.grid(row=4, column=0)

        # Next button
        self.next_button = Button(self.game_box, width=15, height=1, text="next", background="black", fg="yellow",
                                  command=lambda: self.to_next(my_list))
        self.next_button.grid(row=6, column=0, pady=10)

        # Disable the next button
        self.next_button.config(state=DISABLED)
        self.to_next(my_list)

    # check answer
    def reveal_answer(self, location):

        # Disable all the buttons
        self.top_left_button.config(state=DISABLED)
        self.top_right_button.config(state=DISABLED)
        self.bottom_left_button.config(state=DISABLED)
        self.bottom_right_button.config(state=DISABLED)

        # Enable the next_button again
        self.next_button.config(state=NORMAL)

        # Rounds played as game played
        self.rounds_played += 1

        # Check
        if location == self.answer:
            self.answer_label.config(text="Nice!!!", fg="#00FF00")
            self.result += 1
        else:
            self.answer_label.config(text="Maybe Next Time??", fg="#0000FF")

        # refreshed result after right or wrong
        self.result_label.config(text="{} correct / {} roundsplayed".format(self.result, self.rounds_played))

        # To Next defined

    # the next function
    def to_next(self, list):
        self.top_left_button.config(state=NORMAL)
        self.top_right_button.config(state=NORMAL)
        self.bottom_left_button.config(state=NORMAL)
        self.bottom_right_button.config(state=NORMAL)
        self.next_button.config(state=DISABLED)
        self.answer_label.config(text="")

        # Randomized four gods from list again
        question_answer = random.choice(list)
        nope = random.choice(list)
        no = random.choice(list)
        close = random.choice(list)

        # defining variables, correct and wrong answer defined again
        self.question = question_answer[1]
        self.answer = question_answer[0]
        incorrect_answer_1 = nope[0]
        incorrect_answer_2 = no[0]
        incorrect_answer_3 = close[0]
        print(question_answer)

        self.egyptian_god_label.config(text=self.question)

        # Answer List again
        answer_list = [self.answer, incorrect_answer_1, incorrect_answer_2, incorrect_answer_3]
        random.shuffle(answer_list)

        # Define said answer again
        self.top_left = answer_list[0]
        self.top_right = answer_list[1]
        self.bottom_right = answer_list[2]
        self.bottom_left = answer_list[3]

        # Defining the randomized list
        # Top level
        self.top_left_button.config(text=self.top_left, command=lambda: self.reveal_answer(self.top_left))

        self.top_right_button.config(text=self.top_right, command=lambda: self.reveal_answer(self.top_right))

        # Bottom level
        self.bottom_left_button.config(text=self.bottom_left, command=lambda:
        self.reveal_answer(self.bottom_left))

        self.bottom_right_button.config(text=self.bottom_right, command=lambda:
        self.reveal_answer(self.bottom_right))

        # stats frame
        self.help_stats_frame = Frame(self.game_box)
        self.help_stats_frame.grid(row=5)

        # Help and statistics buttons
        self.start_help_button = Button(self.help_stats_frame, text="Help/Rules",
                                        font="Arial 15 bold",
                                        bg="black", fg="white", width=20,
                                        command=self.to_help)
        self.start_help_button.grid(row=1, column=1)

        self.start_statistics_button = Button(self.help_stats_frame, text="Statistics / Export",
                                              font="Arial 15 bold",
                                              bg="black", fg="white", width=20,
                                              command=lambda: self.to_stats(self.rounds_played,
                                                                           self.game_stat_list))
        self.start_statistics_button.grid(row=1, column=2, padx=10)

        # Quit Button
        self.quit_button = Button(self.game_box, text="Quit", fg="white",
                                  bg="red", font="Arial 12 bold", width=15, height=1,
                                  command=self.to_quit)
        self.quit_button.grid(row=10)

    # Statistics & Export
    def to_stats(self, level):
        Game(self, level)
        # color for background
        background_color = "black"

        self.all_calc_list = []

        # Egyptian god quiz main Screen GUI...
        self.to_stats_frame = Frame(width=300, height=300, bg=background_color,
                                    pady=10)
        self.to_stats_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.Egyptian_God_Quiz_label = Label(self.to_stats_frame, text="Egyptian God Quiz", fg="yellow",
                                             font=("Arial", "16", "bold"),
                                             bg=background_color,
                                             padx=10, pady=10)
        self.Egyptian_God_Quiz_label.grid(row=0)

        # history Button (row 1)
        self.history_button = Button(self.to_stats_frame, text="Information", fg="yellow",
                                     font=("Arial", "8", "bold"),
                                     bg=background_color,
                                     padx=10, pady=10,
                                     command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1)

    # Quit function
    def to_quit(self):
        root.destroy()

    # help function
    def to_help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="The quiz generate a description of a random egyptian god." \
                                          "Try to find out which god it is, you get 4 options." \
                                          "Try to get the most amount of questions right!!"
                                          "May Shai bless you in your endeavour.")

class Help:
    def __init__(self, partner):
        # disable help button
        partner.start_help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press 'x' cross at the top, closes help and 'releases' help button.
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="Arial 15 bold")
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="green",
                                  fg="white",
                                  font="arial" "10" "bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.start_help_button.config(state=NORMAL)
        self.help_box.destroy()

    def history(self, calc_history):
        History(self, calc_history)

class History:
    def __init__(self, partner, calc_history):
        # This color is black
        background = "black"

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (ie: history box)
        self.history_box = Toplevel()

        # If users press 'x' cross at the top, closes history and 'releases' history button.
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation history",
                                 font=("Arial", "15", "bold",), fg="yellow",
                                 bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your most recent calculations ", fg="yellow",

                                  justify=LEFT, width=40, bg=background, wrap=250, padx=10, pady=10)
        self.history_text.grid(row=1)

        # history Output goes here... (Row 2)

        # Generate string from list of calcualtions...

        history_string = ""
        if len(calc_history) >= 7:
            for item in range(0, 7):
                history_string += calc_history[lens(calc_history) - item - 1] + "\n"


        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                               calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here are your most recent calculations ", fg="yellow")

        # Export /Dismiss Buttons Frame (row 3)

        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export", bg=background, fg="yellow",
                                    font="Arial 12 bold",
                                    command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_btn = Button(self.export_dismiss_frame, text="Dismiss", bg=background, fg="yellow",
                                  font="Arial 12 bold", command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=0, column=1)

    def close_history(self, partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, calc_history):
        Export(self, calc_history)

class Export:
    def __init__(self, partner, calc_history):
        print(calc_history)

        # This color is black
        background = "black"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()

        # If users press 'x' cross at the top, closes export and 'releases' export button.
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, bg=background)
        self.export_frame.grid()

        # Set up Export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font=("Arial", "15", "bold",), fg="yellow",
                                 bg=background)
        self.how_heading.grid(row=0)

        # Export text (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename in the box below", fg="yellow",
                                 justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (label, row2)
        self.export_text = Label(self.export_frame, text="If the filename you entered already exists,"
                                                         "it will be overwritten.", justify=LEFT, bg=background,
                                 fg='red', font="Arial 10 italic",
                                 wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save", bg=background, fg="yellow",
                                  command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel", bg=background, fg="yellow",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

    def save_history(self, partner, calc_history):

        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = " (no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            self.save_error_label.config(text="Invalid filename - {}".format(problem))

            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            filename = filename + ".txt"

            f = open(filename, "w+")

            for item in calc_history:
                f.write(item + "\n")

            f.close()

            self.close_export(partner)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Egyptian God Quiz")
    something = Start(root)
    root.mainloop()
