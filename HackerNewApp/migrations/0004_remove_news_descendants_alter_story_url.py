# Generated by Django 4.1.1 on 2022-09-19 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "HackerNewApp",
            "0003_ask_comment_job_poll_pollopt_story_news_author_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="news",
            name="descendants",
        ),
        migrations.AlterField(
            model_name="story",
            name="url",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
