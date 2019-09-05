#!/usr/bin/env python
import random


class Question:
    """Holds the Question information for the game."""
    def __init__(self):
        self.text = "Error"
        self.answer = 0
        self.options = ["Error", "Error", "Error", "Error"]
        self.more_info = ""
        self.source = ""

    def create_rand_options(self):
        """
        We take the answer out of the
        self.options variable get a random number and insert
        the answer back into the self.options variable and
        change the self.answer to the random number.

        :return:
        """
        random.seed()
        rand = random.randint(0, 3)

        opt = self.options[self.answer]
        self.options.remove(opt)

        self.options.insert(rand, opt)
        self.answer = rand

    def check_input(self, user_input, range_max):
        """
        Check the users input.

        :param user_input: The user input to check if it is correct.
        :param range_max: This is the max range of options.
        :return: return 0 if the input is correct, 1 if the input is wrong and 2 if the input is out of range.
        """
        try:
            input_num = int(user_input)
        except ValueError:
            print('Digits only please.')
            input_num = -1

        if input_num > range_max or input_num < 1:
            return 2

        if input_num - 1 == self.answer:
            return 0
        else:
            return 1


if __name__ == "__main__":
    print("Testing Question Class.\n")

    quest = Question()

    print("Testing CheckInput(input)...\n")

    print("Test 1. Checking if an input of 0 will return 2.")
    if quest.check_input(0) != 2:
        print("Error in CheckInput(input) == 0 should be 2.")
        print("input was 0, 0 should return 2.")
    else:
        print("Pass...\n")

    print("Test 2. Checking if an input of 5 will return 2.")
    if quest.check_input(5) != 2:
        print("Error in CheckInput(input) == 0 should be 2.")
        print("input was 0, 0 should return 2.")
    else:
        print("Pass...\n")

    print("Test 3. Checking if an input of 1 will return 0.")
    if quest.check_input(1) != 0:
        print("Error in CheckInput(input) == 1 should be 0.")
        print("input was 1, 1 should return 0.")
    else:
        print("Pass...\n")

    print("Test 4. Checking if an input of 'a' will return 2.")
    if quest.check_input('a') != 2:
        print("Error in CheckInput(input) == True should be False.")
        print("input was 'a', 'a' should return False.")
    else:
        print("Pass...\n")

    print("Testing CreateRandOptions()...\n")

    quest.options = ['Answer', 'Wrong1', 'Wrong2', 'Wrong3']
    quest.create_rand_options()

    print("Test 1. Checking if options are random.")
    if quest.options == ['Answer', 'Wrong1', 'Wrong2', 'Wrong3']:
        print("Error in CreateRandOptions() Options not random.")
        print(str(quest.options))
    else:
        print("Pass..\n")


