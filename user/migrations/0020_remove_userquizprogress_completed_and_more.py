# Generated by Django 5.0.1 on 2024-01-22 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_userquizprogress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userquizprogress',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='userquizprogress',
            name='current_question',
        ),
        migrations.AddField(
            model_name='userquizprogress',
            name='current_question_index',
            field=models.IntegerField(default=0),
        ),
    ]