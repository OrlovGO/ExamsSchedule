# Generated by Django 2.2 on 2023-07-17 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0006_exam_program'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='subject',
        ),
    ]