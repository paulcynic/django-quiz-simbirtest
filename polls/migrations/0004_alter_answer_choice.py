# Generated by Django 3.2.9 on 2022-01-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_answer_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.CharField(choices=[('1', 'one'), ('2', 'two')], max_length=64),
        ),
    ]
