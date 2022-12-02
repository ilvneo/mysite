from django.urls import path

from . import views
#from marc.views import FileDownloadView
app_name = 'marc'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name="answer_create"),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
    path('question/createnew/', views.DocumentCreateView.as_view(), name='new'),
    path("", views.uploadFile, name="uploadFile"),
    path('document_view/<int:question_id>', views.download_view, name='download_view'),
    path('document_download/<int:question_id>/<int:nums>', views.download_file, name='download_file')
    #path('document/<int:question_id>/', FileDownloadView.as_view(), name="download")
]
