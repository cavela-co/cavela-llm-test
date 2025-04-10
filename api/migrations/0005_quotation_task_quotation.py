# Generated by Django 5.1.7 on 2025-04-10 23:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_uploadedfile_questions_uploadedfile_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('moq', models.IntegerField()),
                ('lead_time_days', models.IntegerField()),
                ('payment_terms', models.CharField(max_length=200)),
                ('shipping_method', models.CharField(max_length=200)),
                ('shipping_address', models.TextField()),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.uploadedfile')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='quotation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.quotation'),
        ),
    ]
