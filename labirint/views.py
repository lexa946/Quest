import random
from copy import copy

from django.shortcuts import render, redirect
from .forms import HeroForm, SelectHeroForm

# Create your views here.
from django.views.generic import DetailView

from .models import Page, Ways, Stuff, Images, Hero, Buff

def game_over(request):
    hero = Hero.objects.get(user=request.user, is_selected=True)
    hero.delete()
    return render(request, 'labirint/game_over.html')


def index(request):
    return render(request, 'labirint/main_menu.html')


def rules(request):
    return render(request, 'labirint/rules.html')


def prologue(request):
    return render(request, 'labirint/prologue.html')


class PageView(DetailView):
    model = Page
    template_name = 'labirint/Page.html'
    context_object_name = 'Page'

    def get(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            return redirect('account:login')

        try:
            hero = Hero.objects.get(user=request.user, is_selected=True)
            self.hero = copy(hero)

            page = Page.objects.get(pk=self.kwargs['pk'])

            if page.game_over:
                hero.delete()
            else:
                if page.add_stuff.exists():
                    for stuff in page.add_stuff.all():
                        self.hero.stuffs.add(stuff)
                if page.remove_stuff.exists():
                    for stuff in page.remove_stuff.all():
                        self.hero.stuffs.remove(stuff)
                if page.add_buff.exists():
                    for buff in page.add_buff.all():
                        print(buff)
                        self.hero.buffs.add(buff)



            return super(PageView, self).get(request, *args, **kwargs)

        except Hero.DoesNotExist:
            return redirect('labirint:select_hero')


    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        context['Ways'] = Ways.objects.filter(page_anchor=context['Page'].pk)
        context['Hero'] = self.hero

        if context['Page'].game_over:
            context['over_img'] = Images.objects.get(pk=28)

        if context['Page'].enemy_one:
            context['scroll_history'] = Images.objects.get(pk=31)

        return context


def create_hero(request):
    if request.method == 'POST':
        form = HeroForm(request.POST)
        if form.is_valid():
            form.full_clean()
            characteristic = {
                'stamina': 12 + random.randint(1, 13),
                'skill': 6 + random.randint(1, 7),
                'luck': 6 + random.randint(1, 7),
            }

            hero = Hero()
            hero.user = request.user
            hero.img = random.choice(Images.objects.filter(category__pk=1))
            hero.name = form.cleaned_data['hero_name']
            hero.current_skill = hero.max_skill = characteristic['skill']
            hero.current_stamina = hero.max_stamina = characteristic['stamina']
            hero.current_luck = hero.max_luck = characteristic['luck']
            hero.save()
            hero.stuffs.add(Stuff.objects.get(pk=form.cleaned_data['potions']))
            hero.save()

            return redirect('account:personal_area')
    else:
        form = HeroForm()
    potions = Stuff.objects.filter(pk__in=(1, 2, 3))
    return render(request, 'labirint/create_hero.html', context={
        'form': form,
        'potions': potions,
    })


class AboutHero(DetailView):
    model = Hero
    template_name = 'labirint/about_hero.html'


def select_hero(request):
    heroes = Hero.objects.filter(user_id=request.user.pk)
    if not heroes.exists():
        return redirect('labirint:create_hero')

    if request.method == 'POST':
        form = SelectHeroForm(heroes, request.POST)
        if form.is_valid():
            form.full_clean()
            try:
                old_hero_select = Hero.objects.filter(user_id=request.user.pk).get(is_selected=True)
                old_hero_select.is_selected = False
                old_hero_select.save()
            except Hero.DoesNotExist:
                pass

            hero = Hero.objects.get(pk=form.cleaned_data['selects'])
            hero.is_selected = True
            hero.save()
            return redirect('labirint:prologue')
    return render(request, 'labirint/select_hero.html', context={
        'heroes': heroes,
        'form': SelectHeroForm(heroes),
    })


