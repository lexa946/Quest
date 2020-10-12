from django.urls import path
from .views import index, rules, prologue, PageView, create_hero, AboutHero

app_name = 'labirint'

urlpatterns = [
    path('', index, name='index'),
    path('rules/', rules, name='rules'),
    path('prologue/', prologue, name='prologue'),
    path('step/<int:pk>/', PageView.as_view(), name='step'),
    path('create/', create_hero, name='create_hero'),
    path('hero/<int:pk>/', AboutHero.as_view(), name='hero')
]