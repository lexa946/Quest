from django.shortcuts import render, redirect
from .forms import UserFrom
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserFrom(request.POST)
        if form.is_valid():
            form.full_clean()
            User.objects.create(username=form.data['username'],
                                password=make_password(form.data['password']))



            # form.save(commit=False)
            # form.data['password'] = make_password(form.data['password'])
            # form.save()


            return redirect('account:login')
    else:
        form = UserFrom()
    return render(request, 'registration/registor.html', {
        'form': form,
    })

# Create your views here.
