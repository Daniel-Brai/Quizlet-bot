# Generated by Django 4.1.5 on 2023-01-17 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(max_length=300, verbose_name='Answer'),
        ),
    ]
