from django.contrib import admin
from .models import Score

# Register your models here.
@admin.register(Score)

class ScoreAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'points'
    ]