# Generated by Django 4.1.3 on 2022-11-30 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_solicituddestino'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='h_destino',
            field=models.CharField(default=5243, max_length=40),
            preserve_default=False,
        ),
    ]
