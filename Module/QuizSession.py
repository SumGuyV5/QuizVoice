#!/usr/bin/env python
from Module.Question import Question


class QuizSession:
    """Runs the main control for the game."""

    def __init__(self, questions):
        """init the variables """
        self.score = 0
        self.questions = questions

    def run_session(self):
        """

        :return:
        """
        for i in self.questions:

            i.create_rand_options()

            while True:
                print(i.text)
                count = 1
                print("is it...")
                for op in i.options:
                    print(f'{str(count)} {op}')
                    count = count + 1

                answer = input("press a num\n")

                check = i.check_input(answer)
                if check == 0:
                    print("Your Right!")
                    self.score += 1
                    break
                elif check == 1:
                    print("Your Wrong!")
                    break
                elif check == 2:
                    print("Repeat.")
            print(i.more_info)
            print(i.source)
            print("---------------------------")
        self.session_end()

    def session_end(self):
        """

        :return:
        """
        print("Thank you for playing Quiz!")
        print(f'You Got {str(self.score)} question right!')


if __name__ == "__main__":
    print("Testing... QuizSession Class")
    quiz = QuizSession([Question()])

    quiz.run_session()




