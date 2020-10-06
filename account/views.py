from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from labirint.models import Hero
from .forms import UserFrom


def register(request):
    if request.method == 'POST':
        form = UserFrom(request.POST)
        if form.is_valid():
            form.full_clean()
            User.objects.create(username=form.data['username'],
                                password=make_password(form.data['password']))
            return redirect('account:login')
    else:
        form = UserFrom()
    return render(request, 'registration/registor.html', {
        'form': form,
    })

def personal(request):

    return render(request, 'account/personal_area.html', context={
        'heroes': Hero.objects.filter(user_id=request.user.pk),
    })


class PersonalArea(DetailView):

    model = User
    template_name = 'account/personal_area.html'

    def get_context_data(self, **kwargs):
        context = super(PersonalArea, self).get_context_data(**kwargs)
        context['heroes'] = Hero.objects.filter(user_id=self.request.user.pk)
        return context


# Create your views here.
