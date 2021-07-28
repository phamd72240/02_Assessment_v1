from tkinter import *
from functools import partial  # Prevent unwanted windows
import csv
import random
import re


class Start:
    def __init__(self, partner):
        # Start GUI
        self.start_frame = Frame(padx=10, pady=10, bg="black")
        self.start_frame.grid()

        # background
        background = "black"

        # God Quiz Heading (row 0)
        self.egyptian_god_label = Label(self.start_frame, text="Egyptian Gods Quiz",
                                        font="Arial 15 bold", bg=background, fg="yellow")
        self.egyptian_god_label.grid(row=0)

        # Initial instructions (row 1)
        self.god_instructions_label = Label(self.start_frame, text=" Please choose the amount of "
                                                                   "question you want to answer",
                                            font="Arial 12 italic", fg="yellow", bg=background)
        self.god_instructions_label.grid(row=1)

        # to_quiz button frame
        self.to_quiz_frame = Frame(self.start_frame, bg=background)
        self.to_quiz_frame.grid(row=2)

        # Buttons frame ( row 3)
        self.level_frame = Frame(self.start_frame, bg=background)
        self.level_frame.grid(row=3)

        # Button Font
        button_font = "Oswald 40 bold"

        # Low Questions Button
        self.low_level_button = Button(self.level_frame, text="Play",
                                       font=button_font, bg="black", fg="yellow",
                                       command=lambda: self.to_quiz(1))
        self.low_level_button.grid(row=5, column=0, pady=10, padx=5)

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
        self.result_label = Label(self.game_box, font="Arial 14 bold", fg="black", text="{} correct / {} games played"
                                  .format(self.result, self.rounds_played))

        self.result_label.grid(row=4, column=0)

        # Next button
        self.next_button = Button(self.game_box, width=20, height=1, text="next",
                                  background="black", fg="yellow", font="Arial 14 bold",
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
            self.answer_label.config(text="Nice!!!", fg="dark green")
            self.result += 1
        else:
            self.answer_label.config(text="Maybe Next Time??", fg="blue")

        # refreshed result after right or wrong
        self.result_label.config(text="{} correct / {} rounds played".format(self.result, self.rounds_played))

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
                                        bg="black", fg="yellow", width=20,
                                        command=self.to_help)
        self.start_help_button.grid(row=1, column=1)

        self.start_statistics_button = Button(self.help_stats_frame, text="Statistics",
                                              font="Arial 15 bold",
                                              bg="black", fg="yellow", width=20,
                                              command=self.to_stats)
        self.start_statistics_button.grid(row=1, column=2, padx=10)

        # Quit Button
        self.quit_button = Button(self.game_box, text="Quit", fg="white",
                                  bg="red", font="Arial 15 bold", width=15, height=1,
                                  command=self.to_quit)
        self.quit_button.grid(row=10)

        # This color is black
        background_color = "black"

        self.all_calc_list = [self.result, self.rounds_played]

        # history Button (row 1)
        self.history_button = Button(self.help_stats_frame, text="Egyptian God Quiz Export", fg="yellow",
                                     font="Arial 12 bold", width=20, height=2,
                                     bg=background_color, command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1, padx=10, pady=10)

    # History function
    def history(self, calc_history):
        History(self, calc_history)

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

    def to_stats(self):
        get_stats = Stats(self)
        get_stats.stats_text.configure(text="These are your statistics")


class Help:
    def __init__(self, partner):
        # The color is black
        background = "black"

        # disable help button
        partner.start_help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press 'x' cross at the top, closes help and 'releases' help button.
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions", fg="yellow", bg=background,
                                 font="Arial 15 bold")
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="", fg="yellow", bg=background,
                               justify=LEFT, width=40, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="black",
                                  fg="yellow",
                                  font="arial" "10" "bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.start_help_button.config(state=NORMAL)
        self.help_box.destroy()


class Stats:
    def __init__(self, partner):
        print(Stats)

        # The color is black
        background = "black"

        # result (big thanks to yichen for giving me this idea)
        self.result = partner.result

        # Amounts of game (big thanks to yichen for giving me this idea)
        self.rounds_played = partner.rounds_played

        # disable stats button
        partner.start_statistics_button.config(state=DISABLED)

        # Sets up child window (ie: stats box)
        self.stats_box = Toplevel()

        # If users press 'x' cross at the top, closes stats and 'releases' stats button.
        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        # Set up GUI Frame
        self.stats_frame = Frame(self.stats_box, bg=background)
        self.stats_frame.grid()

        # Set up Help heading (row 0)
        self.stats_heading_label = Label(self.stats_frame, text="Game Statistics", bg="black", fg="yellow",
                                         font="Arial 19 bold")
        self.stats_heading_label.grid(row=0)

        # Stats text (label, row 1)
        self.stats_text = Label(self.stats_frame, text="", bg="black", fg="yellow",
                                justify=LEFT, width=40, wrap=250)
        self.stats_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.stats_frame, text="Dismiss", width=10, bg="black",
                                  fg="yellow",
                                  font="arial" "10" "bold",
                                  command=partial(self.close_stats, partner))
        self.dismiss_btn.grid(row=4, pady=10)

        # Label for results
        self.result_label = Label(self.stats_frame, font="Arial 14 bold", fg="yellow", bg="black",
                                  text="{} correct / {} rounds played".format(self.result,
                                                                              self.rounds_played))
        self.result_label.grid(row=2, column=0)

        # refreshed result after right or wrong
        self.result_label.config(text="{} correct / {} rounds played".format(self.result, self.rounds_played))

    def close_stats(self, partner):
        # Put help button back to normal...
        partner.start_statistics_button.config(state=NORMAL)
        self.stats_box.destroy()


class History:
    def __init__(self, partner, calc_history):

        # result (big thanks to yichen for giving me this idea)
        self.result = partner.result

        # Amounts of game (big thanks to yichen for giving me this idea)
        self.rounds_played = partner.rounds_played

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
        self.history_text = Label(self.history_frame, text="Here are your calculations in the most recent run.",
                                  fg="yellow",
                                  justify=LEFT, width=40, bg=background, wrap=250, padx=10, pady=10)
        self.history_text.grid(row=1)

        # Label for results
        self.result_label = Label(self.history_frame, font="Arial 14 bold", fg="yellow", bg="black",
                                  text="{} correct / {} rounds played".format(self.result,
                                                                              self.rounds_played))
        self.result_label.grid(row=4, column=0)

        # refreshed result after right or wrong
        self.result_label.config(text="{} correct / {} rounds played".format(self.result, self.rounds_played))

        # history Output goes here... (Row 2)
        # Generate string from list of calcualtions...
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

        self.result = partner.result
        self.rounds_played = partner.rounds_played

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
                                 fg='yellow', font="Arial 10 italic",
                                 wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="yellow",
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

        global problem
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
                f.write("You got {}/{} right. Congratulations !!\n".format(self.result, self.rounds_played))

            f.close()

            self.close_export(partner)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Egyptian God Quiz")
    something = Start(root)
    root.mainloop()

# Major thanks to yichen and woojin for helping me out with this project.
# Ms G as well since I received help and used loads of stuff from mystery box.
