from django import forms
from .models import Answer


class AnswerForm(forms.ModelForm):
    quiz = forms.IntegerField()
    question = forms.IntegerField()
    choice = forms.CharField(max_length=64)

    class Meta:
        model = Answer
        fields = ('quiz', 'question', 'choice')
