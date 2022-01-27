from selenium import webdriver
from polls.models import Quiz
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class TestQuizPage(StaticLiveServerTestCase):
    port = 8000
    def setUp(self):
        self.browser = webdriver.Chrome('/usr/local/bin/chromedriver')

    def tearDown(self):
        self.browser.close()

    def test_not_found_is_displayed(self):
        self.browser.get(self.live_server_url)

        # The user requests the page for the fisrt time
        # alert = self.browser.find_element_by_class_name('noproject-wrapper')
        self.assertEquals(self.browser.find_element_by_tag_name('h1').text, 'Not Found')

    def test_button_start_quiz(self):
        quiz = Quiz.objects.create(title='First quiz test')
        self.browser.get(self.live_server_url + reverse('polls:index'))
        button = self.browser.find_element_by_id('push_button')
        button.click()
        test_url = self.live_server_url + reverse('polls:questions', args=[1])
        self.assertEquals(self.browser.current_url, test_url)
