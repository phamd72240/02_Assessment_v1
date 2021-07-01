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

        # Help button
        self.help_button = Button(self.game_box, width=10, height=1, text="help", command=lambda:self.to_help)
        self.help_button.grid(row=5, column=0, pady=2)

        # Next button
        self.next_button = Button(self.game_box, width=10, height=1, text="next", command=lambda:self.to_next(my_list))
        self.next_button.grid(row=6, column=0, pady=2)

        # Disable the next button
        self.next_button.config(state=DISABLED)
        self.to_next(my_list)

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


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Egyptian God Quiz")
    something = Start(root)
    root.mainloop()
