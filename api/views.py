from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads


from labirint.models import Hero, Stuff

@csrf_exempt
def characteristic_manager(request):
    json = loads(request.body)
    hero = Hero.objects.get(pk=json['id'])
    hero.current_skill = json['_currentSkill']
    hero.max_skill = json['maxSkill']
    hero.current_stamina = json['_currentStamina']
    hero.max_stamina = json['maxStamina']
    hero.current_luck = json['_currentLuck']
    hero.max_luck = json['maxLuck']
    hero.provisions = json['_provision']
    hero.money = json['money']
    hero.save()
    return render(request, 'base.html')

@csrf_exempt
def remove_item(request):
    json = loads(request.body)
    hero = Hero.objects.get(pk=json['id'])
    hero.stuffs.remove(Stuff.objects.get(name=json['name']))
    hero.save()
    return render(request, 'base.html')


def game_over(request):
    hero = Hero.objects.get(pk=request.GET.dict()['pk'])
    hero.delete()
    return render(request, 'base.html')


def get_inventory(request):
    hero = Hero.objects.get(pk=request.GET.dict()['pk'])
    inventory = hero.stuffs.all()
    JSON = {index: str(item) for index, item in enumerate(inventory)}
    return JsonResponse(JSON)

def get_buffs(request):
    hero = Hero.objects.get(pk=request.GET.dict()['pk'])
    buffs = hero.buffs.all()
    JSON = {index: str(item) for index, item in enumerate(buffs)}
    return JsonResponse(JSON)


# Create your views here.
