# Generated by Django 4.2.2 on 2024-08-26 03:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("happyPerformerBackend", "0004_alter_custom_forms_alloc"),
    ]

    operations = [
        migrations.CreateModel(
            name="OTPVerification",
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
                ("emp_emailid", models.EmailField(max_length=254, unique=True)),
                ("otp", models.CharField(max_length=6)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "OTP Verification",
                "verbose_name_plural": "OTP Verifications",
            },
        ),
    ]
