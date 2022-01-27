from django.test import SimpleTestCase
from polls.forms import AnswerForm


class TestForms(SimpleTestCase):

    def test_answer_form_valid_data(self):
        form = AnswerForm(data={
            'quiz': 1,
            'question': 0,
            'choice': "['1', '2']"
            })
        self.assertTrue(form.is_valid())

    def test_answer_form_no_data(self):
        form = AnswerForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
