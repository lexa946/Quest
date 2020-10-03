# Generated by Django 3.1.1 on 2020-09-30 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labirint', '0009_page_game_over'),
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название характеристики')),
            ],
        ),
        migrations.CreateModel(
            name='ActionsPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Счетчик')),
                ('characteristic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='labirint.characteristics', verbose_name='Характеристика')),
                ('page_anchor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='labirint.page')),
            ],
        ),
    ]