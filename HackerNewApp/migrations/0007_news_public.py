# Generated by Django 4.1.1 on 2022-09-21 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("HackerNewApp", "0006_alter_news_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="public",
            field=models.BooleanField(default=True),
        ),
    ]
