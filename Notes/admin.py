from django.contrib import admin
from .models import Note, Quiz, Choice
# Register your models here.


class QuizInLine(admin.TabularInline):
    model = Quiz
    extra = 1

class ChoicesInLine(admin.TabularInline):
    model = Choice
    extra = 4

@admin.register(Note)
class Note(admin.ModelAdmin):
    inlines =[QuizInLine]

@admin.register(Quiz)
class Quiz(admin.ModelAdmin):
    inlines = [ChoicesInLine]
