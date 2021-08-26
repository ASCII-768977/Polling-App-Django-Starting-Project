from django.urls import path

from . import views

app_name = 'poll'
urlpatterns = [
    path('', views.index, name='index'),
    path('<question_id>', views.choice, name='choice'),
    path('<question_id>/result/', views.result, name='result'),
    path('<question_id>/vote/', views.vote, name='vote'),
]
