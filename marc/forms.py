from django import forms
from marc.models import Question, Answer
from .models import Document

from django_flatpickr.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput

class QuestionForm(forms.ModelForm):
    # upload = forms.FileField(label='첨부 파일', required=True, widget=forms.FileInput(attrs={'class': 'form'}))
    class Meta:
        model = Question
        fields = ['subject', 'content', 'education_start', 'education_end', 'docfile1', 'docfile2']  # QuestionForm에서 사용할 Question 모델의 속성

        # def get_form(self):
        #     form = super().get_form()
        #     form.fields['education_start'].widget = DateTimePickerInput()
        #     form.fields['education_end'].widget = DateTimePickerInput()
        #     return forms

        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'education_start': DatePickerInput(),
            'education_end': DatePickerInput(),
        }

        labels = {
            'subject': '교육등록',
            'content': '교육내용',
            'education_start': '교육시작',
            'education_end': '교육종료',
            'docfile1': '첨부 파일1',
            'docfile2': '첨부 파일1',
        }

        docfile1 = forms.FileField(label='첨부파일1', help_text='최대 42메가', required=True,
                                   widget=forms.FileInput(attrs={'class': 'form'}))
        docfile2 = forms.FileField(label='첨부파일2', help_text='최대 42메가', required=True,
                                   widget=forms.FileInput(attrs={'class': 'form'}))

        date = forms.DateTimeField(
            input_formats=['%d/%m/%Y %H:%M'],
            widget=forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'
            })
        )

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
    upload = forms.FileField(label='첨부 파일', help_text='최대 42메가 바이트', required=False,
                             widget=forms.FileInput(attrs={'class': 'form'}))

    class Meta:
        model = Document
        exclude = ['attached']
