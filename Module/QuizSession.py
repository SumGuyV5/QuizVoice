#!/usr/bin/env python
from Module.Question import Question
from Module.TTS import TTS
from Module.STT import STT


class QuizSession:

    """Runs the main control for the game."""

    def __init__(self, questions):
        """
        init the variables pass False to TTS obj to use print over TTS
        :param questions: the list of quests to ask the user.
        """
        self.tts = TTS()
        self.stt = STT()
        self.score = 0
        self.questions = questions

    def run_session(self):
        """

        :return:
        """
        for i in self.questions:

            i.create_rand_options()

            while True:
                self.tts.say(i.text)
                self.tts.say("is it...")
                for idx, op in enumerate(i.options):
                    self.tts.say(op, str(idx + 1))

                answer = self.stt.speech_rec("press num\n", i.options)

                check = i.check_input(answer, len(i.options))
                if check == 0:
                    self.tts.say("Your Right!")
                    self.score += 1
                    break
                elif check == 1:
                    self.tts.say("Your Wrong!")
                    break
                elif check == 2:
                    self.tts.say("Repeat.")

            print(i.more_info)
            print(i.source)
            print("---------------------------")
        self.session_end()

    def session_end(self):
        """

        :return:
        """
        self.tts.say("Thank you for playing Quiz Voice!")
        self.tts.say(f'You Got {str(self.score)} questions right!')


if __name__ == "__main__":
    print("Testing... QuizSession Class")
    quiz = QuizSession([Question()])

    quiz.run_session()




