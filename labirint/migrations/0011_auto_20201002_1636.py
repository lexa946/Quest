# Generated by Django 3.1.1 on 2020-10-02 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labirint', '0010_actionspage_characteristics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя игрока')),
                ('current_skill', models.IntegerField(verbose_name='Текущее значение мастерства')),
                ('max_skill', models.IntegerField(verbose_name='Максимальное значение мастерства')),
                ('current_stamina', models.IntegerField(verbose_name='Текущее значение выносливости')),
                ('max_stamina', models.IntegerField(verbose_name='Максимальное значение выносливости')),
                ('current_luck', models.IntegerField(verbose_name='Текущее значение удачи')),
                ('max_luck', models.IntegerField(verbose_name='Максимальное значение удачи')),
                ('provisions', models.IntegerField(default=10, verbose_name='Количество провизии')),
                ('money', models.IntegerField(default=0, verbose_name='Количество монет')),
            ],
            options={
                'verbose_name': 'Игрок',
                'verbose_name_plural': 'Игроки',
            },
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.AlterModelOptions(
            name='actionspage',
            options={'verbose_name': 'Действие', 'verbose_name_plural': 'Действия'},
        ),
        migrations.AlterModelOptions(
            name='characteristics',
            options={'verbose_name': 'Характеристика', 'verbose_name_plural': 'Характеристики'},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'Страница', 'verbose_name_plural': 'Страницы'},
        ),
        migrations.AlterField(
            model_name='stuff',
            name='description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='hero',
            name='stuffs',
            field=models.ManyToManyField(to='labirint.Stuff', verbose_name='Рюкзак'),
        ),
    ]
