# Generated by Django 4.1 on 2024-02-11 02:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('NASA', '0002_alter_store_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
