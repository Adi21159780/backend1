# Generated by Django 4.2.2 on 2025-02-22 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("happyPerformerBackend", "0021_alter_kra_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="Calendar",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_start", models.DateTimeField()),
                ("date_end", models.DateTimeField()),
                ("event_type", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "event_title",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("color_hex", models.CharField(blank=True, max_length=7, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "email",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="happyPerformerBackend.employee",
                    ),
                ),
            ],
        ),
    ]
