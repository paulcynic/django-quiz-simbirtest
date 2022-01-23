import json
from typing import List, Union
from .forms import AnswerForm
from .models import Quiz, Question, Answer
from django.db.models import Count, Q


def save_answer_form(request, answer_form: AnswerForm) -> None:
    answer_form_cleaned = answer_form.clean()
    choices = request.POST.getlist('choice')
    answer_form_cleaned['choice'] = choices
    db_form = Answer(
            quiz=answer_form_cleaned['quiz'],
            question=answer_form_cleaned['question'],
            choice=answer_form_cleaned['choice'])
    db_form.save()


def get_right_answers(quiz_id: int) -> List:
    quiz = Quiz.objects.get(id=quiz_id)
    question_list = quiz.question_set.all()
    right_answer_list = []
    for question in question_list:
        choice_list = question.choice_set.filter(is_correct=True)
        right_answer_list.append(
            (question.id, [choice.id for choice in choice_list]))
    return right_answer_list


def sort_questions(question_list: List[Question]) -> List[Question]:
    return question_list.annotate(
            correct_num=Count('choice', filter=Q(choice__is_correct=True))
            ).order_by('correct_num')


def get_page_num(request) -> int:
    if request.method == 'GET':
        page_num = int(request.GET.get('page', 1))
    elif request.method == 'POST':
        page_num = int(request.POST.get('page', 1))
    else:
        page_num = 1
    return page_num


def get_template(ord_list, page_num: Union[int, str]) -> str:
    try:
        if ord_list[int(page_num)-1].correct_num in [0, 1]:
            return 'polls/question_list.html'
        else:
            return 'polls/checkbox.html'
    except IndexError:
        return 'polls/question_list.html'


def get_client_answers(quiz_id: int) -> List:
    quiz = Quiz.objects.get(id=quiz_id)
    question_list = quiz.question_set.all()
    client_answers = Answer.objects.filter(quiz=quiz_id)
    answer_list = []
    for question in question_list:
        answer = client_answers.filter(
                question=question.id).order_by('-id')[0]
        answer_list.append((question.id, answer.choice))
    return [(a, json.loads(b.replace("'", ""))) for a, b in answer_list]


def compute_result(answer_list, right_answer_list) -> float:
    result_list = [x for x in answer_list if x in right_answer_list]
    result_percent = len(result_list) / len(right_answer_list)
    return result_percent


def get_result(quiz_id: int) -> float:
    client_answer_list = (get_client_answers(quiz_id))
    right_answer_list = (get_right_answers(quiz_id))
    result = compute_result(client_answer_list, right_answer_list)
    return result
