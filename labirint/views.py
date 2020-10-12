import random

from django.shortcuts import render, redirect
from .forms import HeroForm

# Create your views here.
from django.views.generic import DetailView

from .models import Page, Ways, Stuff, Images, Hero


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

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        context['Ways'] = Ways.objects.filter(page_anchor=context['Page'].pk)
        if context['Page'].game_over:
            context['over_img'] = Images.objects.get(pk=28)

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

