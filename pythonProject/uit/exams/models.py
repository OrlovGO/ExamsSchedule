from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Subject(models.Model):
    subject_name = models.CharField('subject', max_length=50)

    def __str__(self):
        return f'{self.subject_name}'

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

class Exam(models.Model):
    test = 'test'
    interview = 'interview'
    creative_test = 'creative_test'

    TYPE_CHOICES = [
        (test, 'тест'),
        (interview, 'собеседование'),
        (creative_test, 'творческое испытание')
    ]
    subject = models.ManyToManyField(Subject)
    type = models.CharField('type', max_length=50, choices=TYPE_CHOICES)
    score_min = models.IntegerField('score', default=100, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    program = models.ForeignKey('Program', default=0, on_delete=models.PROTECT)

    def subjects(self):
        return ", ".join([str(p) for p in self.subject.all()])

    def __str__(self):
        return f'{self.subject.all()}'

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'

class Schedule(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.PROTECT)
    date = models.DateField('date')
    time = models.TimeField('time')
    address = models.CharField('address', max_length=50)

    def __str__(self):
        return f'{self.exam}'

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'

class Program(models.Model):
    file = models.URLField('file')

    def __str__(self):
        return f'{self.file}'

    class Meta:
        verbose_name = 'Программа для подготовки'
        verbose_name_plural = 'Программы для подготовки'

