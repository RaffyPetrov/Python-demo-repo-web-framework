from django.shortcuts import render
from django.views import generic as views

from demo_app.web.models import Item


# Create your views here.


class IndexView(views.ListView):
    template_name = 'index.html'
    model = Item
