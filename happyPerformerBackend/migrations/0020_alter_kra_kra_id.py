# Generated by Django 4.2.2 on 2025-02-20 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("happyPerformerBackend", "0019_alter_attendance_date_updated_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kra",
            name="kra_id",
            field=models.ForeignKey(
                blank=True,
                db_column="kra_id",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="happyPerformerBackend.kra_table",
            ),
        ),
    ]
