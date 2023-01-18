"""quizlet URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from quizlet.quiz.views import RandomQuestionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/random_question/', RandomQuestionView.as_view(), name="random_question")
]
