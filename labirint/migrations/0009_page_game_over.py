# Generated by Django 3.1.1 on 2020-09-30 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labirint', '0008_auto_20200930_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='game_over',
            field=models.BooleanField(default=False, verbose_name='Конец игры?'),
        ),
    ]
