from django.contrib import admin
from .models import Subject, Exam, Schedule, Program

# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_name']
    list_editable = ['subject_name']
    list_display_links = None

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['subjects', 'type', 'score_min']
    #list_editable = ['subject', 'type', 'score_min']
    list_display_links = None

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['exam', 'date', 'time', 'address']
    list_editable = ['exam', 'date', 'time', 'address']
    list_display_links = None

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['file']
    list_editable = ['file']
    list_display_links = None

