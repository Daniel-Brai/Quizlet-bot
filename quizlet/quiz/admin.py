from django.contrib import admin
from .models import Question, Answer

class AnswerInline(admin.TabularInline): # new
    model = Answer
    fields = ["answer", "is_correct"]

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)

