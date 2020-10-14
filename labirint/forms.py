from django import forms


class HeroForm(forms.Form):
    hero_name = forms.CharField(label="Имя персонажа", max_length=100)

    choice_set = [(1, "Напиток Мудрых"),
                  (2, "Напиток Сильных"),
                  (3, "Напиток Удачливых"),
                  ]
    potions = forms.ChoiceField(choices=choice_set, label="Выберите начальный элексир", widget=forms.RadioSelect)


class SelectHeroForm(forms.Form):
    def __init__(self, heroes, *args, **kwargs):
        self.heroes = heroes
        super(SelectHeroForm, self).__init__(*args, **kwargs)
        choice_set = []
        for hero in heroes:
            choice_set.append((hero.pk, hero))
        self.fields['selects'].choices = choice_set

    selects = forms.ChoiceField(widget=forms.RadioSelect, label="Выберите Героя",)

