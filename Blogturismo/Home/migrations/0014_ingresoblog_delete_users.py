# Generated by Django 4.1.3 on 2022-12-06 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0013_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngresoBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_nombre', models.CharField(max_length=40)),
                ('b_titulo', models.CharField(max_length=40)),
                ('b_lugar', models.CharField(max_length=40)),
                ('b_comentario', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='users',
        ),
    ]
