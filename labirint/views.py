from django.shortcuts import render


# Create your views here.
from django.views.generic import DetailView

from .models import Page, Ways

def index(request):
    return render(request, 'labirint/main_menu.html')


def rules(request):
    return render(request, 'labirint/rules.html')


def prologue(request):
    return render(request, 'labirint/prologue.html')


class PageView(DetailView):
    model = Page
    template_name = 'labirint/Page.html'
    context_object_name = 'Page_ways'

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        context['Ways'] = Ways.objects.filter(page_anchor=context['Page_ways'].pk)
        return context