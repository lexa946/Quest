# Generated by Django 3.1.1 on 2020-10-08 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labirint', '0015_auto_20201007_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category', to='labirint.entitycategory', verbose_name='Категория'),
        ),
    ]
