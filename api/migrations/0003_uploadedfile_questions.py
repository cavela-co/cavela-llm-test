# Generated by Django 5.1.7 on 2025-03-20 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_uploadedfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='questions',
            field=models.JSONField(blank=True, help_text='A JSON list of questions related to this file', null=True),
        ),
    ]
