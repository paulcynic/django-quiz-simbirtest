from django.urls import path
from .views import index, get_answer, final_result, remove_answers


app_name = 'polls'
urlpatterns = [
    path('', index, name='index'),
    path('quiz/<int:quiz_id>/', get_answer, name='questions'),
    path('quiz/<int:quiz_id>/result/', final_result, name='results'),
    path('quiz/<int:quiz_id>/result/clean/',
         remove_answers, name='remove_answers'),
]
