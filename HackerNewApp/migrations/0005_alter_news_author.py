# Generated by Django 4.1.1 on 2022-09-20 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("HackerNewApp", "0004_remove_news_descendants_alter_story_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="author",
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]