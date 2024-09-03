# Generated by Django 5.0.4 on 2024-09-03 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happyPerformerBackend', '0002_kra_measurement_kra_submission_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='sop',
            name='ratings',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=1, null=True),
        ),
        migrations.AddField(
            model_name='sop',
            name='remarks',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='sop',
            name='selfratings',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='kra',
            name='ratings',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=1, null=True),
        ),
    ]
