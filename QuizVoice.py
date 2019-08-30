#!/usr/bin/env python
from Module.QuizXMLSetup import QuizXMLSetup

if __name__ == "__main__":
    quiz = QuizXMLSetup()

    ses = quiz.quiz_session_setup(5)
    ses.run_session()
