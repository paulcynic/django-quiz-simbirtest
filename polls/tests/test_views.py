from django.test import TestCase, Client
from django.urls import reverse
from polls.models import Quiz, Question, Choice, Answer
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.quiz1 = Quiz.objects.create(title="First quiz")
        self.question1 = Question.objects.create(
                question_text="who is bigger?", quiz=self.quiz1)
        self.question2 = Question.objects.create(
                question_text="second question?", quiz=self.quiz1)
        self.choice1 = Choice.objects.create(choice_text="A mouse",
                question=self.question1)
        self.choice2 = Choice.objects.create(choice_text="An elephant",
                question=self.question1, is_correct=True)
        self.index_url = reverse('polls:index')
        quiz_id = self.quiz1.id
        self.get_answer_url = reverse('polls:questions', args=[quiz_id])
        self.final_result_url = reverse('polls:results', args=[quiz_id])
        self.remove_answers_url = reverse('polls:remove_answers',
                                          args=[quiz_id])

    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'polls/index.html',
                                'polls/main.html')

    def test_get_answer_GET(self):
        response = self.client.get(self.get_answer_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/question_list.html')

    def test_get_answer_POST(self):
        response = self.client.post(self.get_answer_url, {
            'quiz': self.quiz1.id,
            'question': self.question1.id,
            'choice': self.choice2.id
            })
        self.assertEquals(json.loads(
            Answer.objects.first().choice.replace("'", "")
            ), [self.choice2.id])
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/question_list.html')

    def test_get_answer_POST_no_data(self):
        response = self.client.post(self.get_answer_url)
        self.assertEquals(Answer.objects.count(), 0)
        self.assertTemplateUsed(response, 'polls/question_list.html')

    def test_remove_answers_GET(self):
        response = self.client.get(self.remove_answers_url)
        self.assertEquals(response.status_code, 302)
