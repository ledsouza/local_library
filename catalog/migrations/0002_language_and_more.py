# Generated by Django 5.0.4 on 2024-04-26 10:27

import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)", max_length=200, unique=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='language',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='language_name_case_insensitive_unique', violation_error_message='Language already exists (case insensitive match)'),
        ),
    ]
