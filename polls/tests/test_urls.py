from django.test import SimpleTestCase
from django.urls import reverse, resolve
from polls.views import index, get_answer, final_result, remove_answers


class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('polls:index')
        self.assertEquals(resolve(url).func, index)

    def test_get_answer_url_resolves(self):
        url = reverse('polls:questions', args=[1])
        self.assertEquals(resolve(url).func, get_answer)

    def test_final_result_url_resolves(self):
        url = reverse('polls:results', args=[1000200202020])
        self.assertEquals(resolve(url).func, final_result)

    def test_list_url_is_resolved(self):
        url = reverse('polls:remove_answers', args=[99])
        self.assertEquals(resolve(url).func, remove_answers)
        # self.assertEquals(resolve(url).func.view_class, MyDeleteView)
