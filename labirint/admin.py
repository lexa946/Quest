from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Page, Hero, Enemy, Ways, Stuff, Characteristics, Images, EntityCategory, Buff


# Register your models here.

class WaysInline(admin.StackedInline):
    model = Ways
    extra = 1



class PageAdmin(admin.ModelAdmin):
    list_display = ['id', 'short_desc']
    list_display_links = ['id', 'short_desc']
    list_editable = []
    search_fields = ['id__iexact', ]
    inlines = [WaysInline]
    list_per_page = 5
    save_on_top = True


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'skill', 'stamina', 'luck', 'get_image']
    list_display_links = ['user', 'name']
    readonly_fields = ['last_step', 'is_selected']

    def skill(self, obj):
        return f'{obj.current_skill}/{obj.max_skill}'
    skill.short_description = 'Мастерство'

    def stamina(self, obj):
        return f'{obj.current_stamina}/{obj.max_stamina}'
    stamina.short_description = 'Выносливость'

    def luck(self, obj):
        return f'{obj.current_luck}/{obj.max_luck}'
    luck.short_description = 'Удача'

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.img.image.url}" width="100"/>')

    get_image.short_description = 'Миниатюра'
    get_image.allow_tags = True


class EnemyAdmin(admin.ModelAdmin):
    list_display = ['name', 'skill', 'stamina', 'get_image']
    search_fields = ['name', ]
    list_per_page = 10

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.img.image.url}" width="100"/>')

    get_image.short_description = 'Миниатюра'
    get_image.allow_tags = True


class StuffAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_display_links = ['name']
    ordering = ['name']

class BuffAdmin(admin.ModelAdmin):
    pass

class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'get_image']
    list_display_links = ['name', ]

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100"/>')

    get_image.short_description = 'Миниатюра'
    get_image.allow_tags = True


class EntityCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Page, PageAdmin)
admin.site.register(Hero, PlayerAdmin)
admin.site.register(Enemy, EnemyAdmin)
admin.site.register(Stuff, StuffAdmin)
admin.site.register(Characteristics, CharacteristicAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(EntityCategory, EntityCategoryAdmin)
admin.site.register(Buff, BuffAdmin)
