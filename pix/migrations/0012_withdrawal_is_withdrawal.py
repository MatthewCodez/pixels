# Generated by Django 5.0.6 on 2024-09-09 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pix', '0011_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawal',
            name='is_withdrawal',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='false', max_length=20),
        ),
    ]
