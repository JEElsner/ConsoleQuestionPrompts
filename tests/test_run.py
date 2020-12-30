import unittest


class TestQuestions(unittest.TestCase):
    def setUp(self):
        import ConsoleQuestionPrompts as questions

        self.questions = questions

    def test_questions_exist(self):
        question = self.questions.ask_question
        some = self.questions.ask_some
        options = self.questions.option_question
        range = self.questions.range_question
        yn = self.questions.yes_no_question

    def test_blank_yes_no_response_question(self):
        response = self.questions.yes_no_question(
            prompt='Just press enter. Dont enter anything',
        )

        self.assertFalse(response)


if __name__ == '__main__':
    unittest.main()
