# Generated by Django 4.2.2 on 2025-02-27 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("happyPerformerBackend", "0022_calendar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tblleaves",
            name="emp_emailid",
            field=models.ForeignKey(
                db_column="emp_emailid",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="happyPerformerBackend.employee",
            ),
        ),
    ]
