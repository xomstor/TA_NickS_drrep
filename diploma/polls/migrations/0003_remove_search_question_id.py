# Generated by Django 5.0.3 on 2024-05-13 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_search'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='question_id',
        ),
    ]
