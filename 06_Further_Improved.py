from tkinter import *
from functools import partial # Prevent unwanted windows
import csv
import random


class Start:
    def __init__(self, partner,):
        # Start GUI
        self.start_frame = Frame(padx=10, pady=10, bg="#D4E1F5")
        self.start_frame.grid()

        # background
        background = "#D4E1F5"

        # God Quiz Heading (row 0)
        self.egyptian_god_label = Label(self.start_frame, text="Egyptian God Quiz",
                                       font="Arial 16 bold", bg=background)
        self.egyptian_god_label.grid(row=0)

        # Initial instructions (row 1)
        self.god_instructions_label = Label(self.start_frame, text=" Please choose the amount of "
                                                                 "question you want to answer",
                                          font="Arial 8 italic", fg="black", bg=background)
        self.god_instructions_label.grid(row=1)

        # to_quiz button frame
        self.to_quiz_frame = Frame(self.start_frame, bg=background)
        self.to_quiz_frame.grid(row=2)

        # Buttons frame ( row 3)
        self.level_frame = Frame(self.start_frame, bg=background)
        self.level_frame.grid(row=3)

        # Button Font
        button_font = "Oswald 12 bold"

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
        self.egyptian_god_label = Label(self.game_frame, text="?",
                                   font="Arial 15")
        self.egyptian_god_label.grid(row=0)

        # Label showing answer
        self.answer_label = Label(self.game_frame, text="", font="Arial 15")
        self.answer_label.grid(row=1)

        # Setup grid for answer buttons row 3
        self.answers_frame = Frame(self.game_box)
        self.answers_frame.grid(row=3)

        # Top level button
        self.top_left_button = Button(self.answers_frame, text="",
                                      font="Arial 15", padx=5, pady=5, width=40,
                                      command=lambda: self.reveal_answer(self.top_left))
        self.top_left_button.grid(column=0, row=0)

        self.top_right_button = Button(self.answers_frame, text="",
                                      font="Arial 15", padx=5, pady=5, width=40,
                                      command=lambda: self.reveal_answer(self.top_right))
        self.top_right_button.grid(column=1, row=0)

        # Bottom level button
        self.bottom_left_button = Button(self.answers_frame, text="",
                                      font="Arial 15", padx=5, pady=5, width=40,
                                      command=lambda: self.reveal_answer(self.bottom_left))
        self.bottom_left_button.grid(column=0, row=1)

        self.bottom_right_button = Button(self.answers_frame, text="",
                                      font="Arial 15", padx=5, pady=5, width=40,
                                      command=lambda: self.reveal_answer(self.bottom_right))
        self.bottom_right_button.grid(column=1, row=1)

        # Label for results
        self.result_label = Label(self.game_box, text="{} correct / {} roundsplayed".format(self.result,
                                                                                            self.rounds_played))
        self.result_label.grid(row=4)

        # Next button
        self.next_button = Button(self.game_box, width=10, height=1, text="next",
                                  command=lambda:self.to_next(my_list))
        self.next_button.grid(row=6, column=0, pady=2)

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

        # Help and Game Stats button (row 5)
        self.start_help_frame = Frame(self.game_frame, pady=10)
        self.start_help_frame.grid(row=5)

        # Help and statistics buttons
        self.start_help_button = Button(self.start_help_frame, text="Help/Rules",
                                        font="Arial 15 bold",
                                        bg="black", fg="white",
                                        command=self.to_help)
        self.start_help_button.grid(row=1, column=1)

        self.start_statistics_button = Button(self.start_help_frame, text="Statistics / Export",
                                              font="Arial 15 bold",
                                              bg="white", fg="black",
                                              command=lambda: self.to_stats(self.rounds_played,
                                                                            self.game_stats_list))
        self.start_statistics_button.grid(row=1, column=2, padx=2)

        # Quit Button
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                  bg="red", font="Arial 12 bold", width=3, height=1,
                                  command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=10, pady=10)

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


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Egyptian God Quiz")
    something = Start(root)
    root.mainloop()
