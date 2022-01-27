from django.test import TestCase
from polls.models import Quiz


class TestModels(TestCase):

    def setUp(self):
        self.quiz = Quiz.objects.create(
                title="Test Quiz"
                )

    def test_quiz_title_is_created(self):
        self.assertEquals(self.quiz.title, "Test Quiz")
