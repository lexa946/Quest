from django.urls import path
from .views import index, rules, prologue, PageView

app_name = 'labirint'

urlpatterns = [
    path('', index, name='index'),
    path('rules/', rules, name='rules'),
    path('prologue/', prologue, name='prologue'),
    path('step/<int:pk>', PageView.as_view(), name='step'),
]