# Generated by Django 3.2.9 on 2022-01-18 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['pk']},
        ),
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.CharField(max_length=64),
        ),
    ]