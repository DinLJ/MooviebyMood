# Generated by Django 4.2.6 on 2024-03-05 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TemporaryRating",
            fields=[
                ("userId", models.IntegerField()),
                (
                    "movieId",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="api.movie",
                    ),
                ),
                ("rating", models.FloatField()),
                ("expires_at", models.DateTimeField()),
            ],
        ),
    ]
