# Generated by Django 3.2.9 on 2022-01-18 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20220118_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.JSONField(),
        ),
    ]
