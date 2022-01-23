from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Quiz, Answer
from .forms import AnswerForm
from .services import (
        get_template,
        get_page_num,
        save_answer_form,
        sort_questions,
        get_result)
from django.urls import reverse


def index(request):
    quiz = Quiz.objects.first()
    return render(request, 'polls/index.html', {'quiz': quiz})


def get_answer(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    question_list = quiz.question_set.all()
    # Сортирует список вопросов: сначала с одним ответом, затем с двумя
    ord_list = sort_questions(question_list)
    # Создает страницы соответственно количеству вопросов
    paginator = Paginator(ord_list, 1)
    page_num = get_page_num(request)
    page = paginator.get_page(page_num)
    context = {'questions': page.object_list,
               'page': page,
               'quiz': quiz}
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            print('form is valid!')
            if answer_form.has_changed():
                '''Меняет поле choice из списка в строку,
                сохраняет форму'''
                save_answer_form(request, answer_form)
                print('form was saved')
            if page.has_next():
                page = paginator.get_page(page.next_page_number())
                context = {'questions': page.object_list,
                           'page': page,
                           'quiz': quiz}
                return render(request,
                              get_template(ord_list,
                                           (int(page_num) + 1)),
                              context)
            else:  # Нет следующей страницы, вопросы закончились
                return HttpResponseRedirect(reverse(
                                            'polls:results',
                                            kwargs={'quiz_id': quiz.id}))
        else:
            print('form invalid!!!')
            return render(request,
                          get_template(ord_list, (page_num)),
                          context)
    # Если идёт запрос методом GET
    return render(request,
                  get_template(ord_list, (page_num)),
                  context)


def final_result(request, quiz_id):
    result = get_result(quiz_id)
    return render(request,
                  'polls/result.html',
                  {'result': result, 'quiz_id': quiz_id})


def remove_answers(request, quiz_id):
    Answer.objects.filter(quiz=quiz_id).delete()
    return HttpResponseRedirect(reverse('polls:index'))
