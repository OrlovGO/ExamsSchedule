# Generated by Django 2.2 on 2023-07-17 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0005_auto_20230714_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='program',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='exams.Program'),
        ),
    ]