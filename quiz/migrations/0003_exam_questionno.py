# Generated by Django 3.2 on 2021-10-13 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_rename_corrans_exam_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='QuestionNo',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
