# Generated by Django 3.1.1 on 2020-09-29 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labirint', '0002_enemy_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enemy',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Название противника'),
        ),
    ]