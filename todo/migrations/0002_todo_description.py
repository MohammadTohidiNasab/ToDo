# Generated by Django 4.1.7 on 2023-03-22 15:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="Description",
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
