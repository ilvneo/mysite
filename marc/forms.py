from django import forms
from marc.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content'] # QuestionForm에서 사용할 Question 모델의 속성
        