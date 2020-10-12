from django import forms



class HeroForm(forms.Form):
    hero_name = forms.CharField(label="Имя персонажа", max_length=100)

    choice_set = [(1, "Напиток Мудрых"),
                  (2, "Напиток Сильных"),
                  (3, "Напиток Удачливых")]
    potions = forms.ChoiceField(choices=choice_set,
                                label="Выберите начальный элексир", widget=forms.RadioSelect)
