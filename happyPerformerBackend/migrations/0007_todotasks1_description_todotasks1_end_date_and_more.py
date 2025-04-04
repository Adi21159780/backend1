# Generated by Django 4.2.2 on 2025-02-13 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("happyPerformerBackend", "0006_reaction"),
    ]

    operations = [
        migrations.AddField(
            model_name="todotasks1",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="todotasks1",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="todotasks1",
            name="priority",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="todotasks1",
            name="start_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
