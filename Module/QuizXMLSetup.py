#!/usr/bin/env python
import os
import random

from Module.Question import Question
from Module.QuizSession import QuizSession

from xml.dom.minidom import parse


class QuizXMLSetup:
    """Loads and xml file with the Questions"""

    def __init__(self):
        self._dom = object

        self.questions = []
        self.num = 0

        self.read_file(os.path.join(os.getcwd(), 'xml', 'quiz.xml'))

        self.num = len(self.questions)

    def quiz_session_setup(self, how_many):
        """

        :param how_many: how many questions to generate.
        :return: returns a QuizSession Object
        """
        random.seed()

        """if there less questions available
        we change how_many variable to self.num"""
        if self.num < how_many:
            how_many = self.num

        nums_list = []

        count = 1
        while True:
            if self.num > 0:
                rand = random.randrange(0, self.num)
            else:
                rand = 0

            if nums_list.count(rand) == 0:
                nums_list.append(rand)
                count += 1

            if count > how_many:
                break  # exit the while loop

        temp = []
        for num in nums_list:
            temp.append(self.questions[num])

        session = QuizSession(temp)

        return session

    def read_file(self, filename):
        """

        :param filename: The name of the XML file.
        :return:
        """
        try:
            self._dom = parse(filename)
        except IOError:
            print(f'File IO Error on file name {filename}')

        questions = self._dom.getElementsByTagName("Question")
        for question in questions:
            self._load_question(question)

    def _load_question(self, question):
        """
        Loads up the Question xml tag into a
        Question Object and calls _load_answers and _load_facts.
        :param question: xml element
        :return:
        """
        text = question.getElementsByTagName("Text")[0].firstChild.nodeValue

        options = self._load_options(question)

        facts = self._load_facts(question)

        quest = Question()
        quest.text = text
        quest.options = options
        quest.more_info = facts[0]
        quest.source = facts[1]
        self.questions.append(quest)

    @staticmethod
    def _load_options(question):
        """
        Loads up the Options xml tag info a list and returns it.

        :param question: xml element
        :return: Answers list
        """
        answer_list = []
        options = question.getElementsByTagName("Option")
        for option in options:
            if option.getElementsByTagName("Answer").length > 0:
                answer_list.insert(0, option.firstChild.nodeValue)
            else:
                answer_list.append(option.firstChild.nodeValue)

        return answer_list

    @staticmethod
    def _load_facts(question):
        """
        Loads up the facts and source xml tag into a list and returns it.

        :param question: xml element
        :return: Facts list
        """
        facts_list = []

        fact = ""
        source = ""

        for f in question.getElementsByTagName("Facts"):
            fact = f.firstChild.nodeValue
            break

        for s in question.getElementsByTagName("Source"):
            source = s.firstChild.nodeValue
            break

        facts_list.append(fact)
        facts_list.append(source)

        return facts_list


if __name__ == "__main__":
    quiz = QuizXMLSetup()
    i = quiz.quiz_session_setup(5)
