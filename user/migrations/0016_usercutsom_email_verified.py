# Generated by Django 5.0.1 on 2024-01-19 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_remove_user_answer_quiz_attempt_delete_quizattempt'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercutsom',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
    ]
