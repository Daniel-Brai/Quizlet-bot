# Generated by Django 4.1.5 on 2023-01-18 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_answer_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Title'),
        ),
    ]
