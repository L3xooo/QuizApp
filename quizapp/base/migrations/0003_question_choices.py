# Generated by Django 4.1.6 on 2023-02-05 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_question_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='choices',
            field=models.JSONField(default=''),
        ),
    ]
