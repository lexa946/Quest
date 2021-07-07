from django.urls import path

from .views import characteristic_manager, game_over, get_inventory, get_buffs, remove_item

app_name = 'api'
urlpatterns = [
    path('hero/remove/item/', remove_item),
    path('hero/characteristic/', characteristic_manager),
    path('hero/inventory/', get_inventory),
    path('hero/buffs/', get_buffs),
    path('gameover/', game_over),
]

