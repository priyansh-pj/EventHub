# Generated by Django 4.2.1 on 2023-05-27 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="image",
            field=models.ImageField(
                blank=True, default="events/event.png", null=True, upload_to="events/"
            ),
        ),
    ]
