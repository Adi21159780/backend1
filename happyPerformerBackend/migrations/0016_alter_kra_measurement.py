# Generated by Django 4.2.2 on 2025-02-18 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("happyPerformerBackend", "0015_alter_kra_ratings_scale"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kra",
            name="measurement",
            field=models.CharField(default=0, null=True),
        ),
    ]
