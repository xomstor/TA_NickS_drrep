# Generated by Django 5.0.3 on 2024-05-13 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_search_question_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='question_text',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='search',
            name='search_query',
            field=models.TextField(),
        ),
    ]
