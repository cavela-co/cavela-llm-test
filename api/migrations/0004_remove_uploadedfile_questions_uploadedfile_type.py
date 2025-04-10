# Generated by Django 5.1.7 on 2025-04-10 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_uploadedfile_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedfile',
            name='questions',
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='type',
            field=models.CharField(choices=[('QUOATATION', 'Quoatation'), ('PROD_SPEC', 'Prod Spec'), ('QA_REPORT', 'Qa Report'), ('OTHER', 'Other')], max_length=20, null=True),
        ),
    ]
