# Generated by Django 5.0.4 on 2024-09-11 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happyPerformerBackend', '0003_sop_ratings_sop_remarks_sop_selfratings_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pan',
            name='pan_no',
            field=models.CharField(max_length=30),
        ),
    ]
