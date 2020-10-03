from django.contrib import admin
from .models import Page, Hero, Enemy, Ways, Stuff, ActionsPage, Characteristics


# Register your models here.

class WaysInline(admin.StackedInline):
    model = Ways
    extra = 1


class ActionInline(admin.StackedInline):
    model = ActionsPage
    extra = 1


class PageAdmin(admin.ModelAdmin):
    list_display = ['id', 'short_desc']
    list_display_links = ['id', 'short_desc']
    list_editable = []
    search_fields = ['id__iexact', ]
    inlines = [WaysInline, ActionInline]
    list_per_page = 5
    save_on_top = True


class PlayerAdmin(admin.ModelAdmin):
    pass


class EnemyAdmin(admin.ModelAdmin):
    list_display = ['name', 'skill', 'stamina', ]
    search_fields = ['name', ]


class StuffAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_display_links = ['name']
    ordering = ['name']


class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

admin.site.register(Page, PageAdmin)
admin.site.register(Hero, PlayerAdmin)
admin.site.register(Enemy, EnemyAdmin)
admin.site.register(Stuff, StuffAdmin)
admin.site.register(Characteristics, CharacteristicAdmin)
