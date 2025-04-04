# Generated by Django 4.2.2 on 2025-02-20 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("happyPerformerBackend", "0017_alter_kra_measurement_alter_kra_ratings_scale"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendance",
            name="date_updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="datetime_log",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="emp_emailid",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="happyPerformerBackend.employee",
            ),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="latitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="log_type",
            field=models.CharField(
                choices=[("IN", "IN"), ("OUT", "OUT")], max_length=3, null=True
            ),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="longitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="user_ip",
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
