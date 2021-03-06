# Generated by Django 4.1a1 on 2022-05-26 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chats", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChatbotData",
            fields=[
                ("idx", models.IntegerField(primary_key=True, serialize=False)),
                ("questions", models.CharField(max_length=255)),
                ("answers_ko", models.CharField(max_length=255)),
                ("labels", models.IntegerField()),
                ("answers_en", models.CharField(max_length=255)),
            ],
        ),
    ]
