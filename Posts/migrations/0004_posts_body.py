# Generated by Django 2.2 on 2020-09-05 03:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0003_auto_20200903_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='body',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
