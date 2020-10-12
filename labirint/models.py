from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Hero(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Пользователь в системе", default=None)
    name = models.CharField(max_length=20, verbose_name="Имя игрока")
    img = models.ForeignKey(to="Images", on_delete=models.PROTECT, verbose_name="Картинка игрока", limit_choices_to={
        "category__pk": 1,
    })
    current_skill = models.IntegerField(verbose_name="Текущее значение мастерства")
    max_skill = models.IntegerField(verbose_name="Максимальное значение мастерства")
    current_stamina = models.IntegerField(verbose_name="Текущее значение выносливости")
    max_stamina = models.IntegerField(verbose_name="Максимальное значение выносливости")
    current_luck = models.IntegerField(verbose_name="Текущее значение удачи")
    max_luck = models.IntegerField(verbose_name="Максимальное значение удачи")
    provisions = models.IntegerField(default=10, verbose_name="Количество провизии")
    money = models.IntegerField(default=0, verbose_name="Количество монет")
    stuffs = models.ManyToManyField('Stuff', verbose_name="Рюкзак")
    is_selected = models.BooleanField(verbose_name="Выбранный?", default=False)
    last_step = models.ForeignKey(to="Page", on_delete=models.DO_NOTHING,
                                  verbose_name="Последний переход", default=1)

    def get_username(self):
        return self.user.username

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'


class EntityCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    class Meta:
        verbose_name = 'Категория существ'
        verbose_name_plural = 'Категории существ'

    def __str__(self):
        return self.name


class Images(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    image = models.ImageField(upload_to="images/", verbose_name="Изображение", )
    category = models.ForeignKey(to=EntityCategory, on_delete=models.PROTECT, verbose_name="Категория",
                                 related_name="category")

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.name


class Enemy(models.Model):
    name = models.CharField(max_length=25, verbose_name="Название противника")
    skill = models.IntegerField(verbose_name="Мастерство")
    stamina = models.IntegerField(verbose_name="Выносливость")
    img = models.ForeignKey(to=Images, verbose_name="Картинка", on_delete=models.SET_DEFAULT,
                            default=Images.objects.get(name="Заглушка").pk, limit_choices_to={
            "category__pk": 2,
        })

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Враг'
        verbose_name_plural = 'Враги'


class Page(models.Model):
    description = models.TextField(verbose_name="Описание")
    enemy_one = models.ForeignKey(Enemy, on_delete=models.PROTECT, null=True, verbose_name='Первый враг', default=None,
                                  blank=True, related_name='enemy_one')
    enemy_two = models.ForeignKey(Enemy, on_delete=models.PROTECT, null=True, verbose_name='Второй Враг', default=None,
                                  blank=True, related_name='enemy_two')
    game_over = models.BooleanField(verbose_name="Конец игры?", default=False)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.description[:10] + '... ' + f'№{str(self.pk)}'

    def short_desc(self):
        return self.description[:50] + '...'
    short_desc.short_description = 'Описание'


class Ways(models.Model):
    page_anchor = models.ForeignKey(Page, on_delete=models.PROTECT)
    description = models.CharField(max_length=255, verbose_name="Описание")
    step = models.IntegerField(verbose_name="ID страницы перехода")

    class Meta:
        verbose_name = 'Путь'
        verbose_name_plural = 'Пути'

    def __str__(self):
        return self.description


class Characteristics(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название характеристики")

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return self.name


class ActionsPage(models.Model):
    page_anchor = models.ForeignKey(Page, on_delete=models.PROTECT)
    characteristic = models.ForeignKey(Characteristics, on_delete=models.PROTECT, verbose_name="Характеристика")
    count = models.IntegerField(verbose_name="Счетчик")

    class Meta:
        verbose_name = 'Действие'
        verbose_name_plural = 'Действия'


class Stuff(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    description = models.CharField(max_length=255, verbose_name="Описание", blank=True)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name
