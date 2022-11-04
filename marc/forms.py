from django import forms
from marc.models import Question, Answer
from .models import Document


class QuestionForm(forms.ModelForm):

    #upload = forms.FileField(label='첨부 파일', required=True, widget=forms.FileInput(attrs={'class': 'form'}))
    class Meta:
        model = Question
        fields = ['subject', 'content', 'docfile1', 'docfile2']  # QuestionForm에서 사용할 Question 모델의 속성

        labels = {
            'subject': '교육등록',
            'content': '교육내용',
            'docfile1': '첨부 파일1',
            'docfile2': '첨부 파일1',
        }

        docfile1 = forms.FileField(label='첨부파일1', help_text='최대 42메가', required=True, widget=forms.FileInput(attrs={'class': 'form'}))
        docfile2 = forms.FileField(label='첨부파일2', help_text='최대 42메가', required=True, widget=forms.FileInput(attrs={'class': 'form'}))

        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10})
        # }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }


class DocumentForm(forms.ModelForm):
    upload = forms.FileField(label='첨부 파일',  help_text='최대 42메가 바이트', required=False, widget=forms.FileInput(attrs={'class': 'form'}))

    class Meta:
        model = Document
        exclude = ['attached']

