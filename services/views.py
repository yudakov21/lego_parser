from django.shortcuts import render
from django.views.generic import ListView
from .models import LegoToy

# Create your views here.
class LegoToyListView(ListView):
    model = LegoToy
    template_name = 'lego/lego_toys.html'
    context_object_name = 'toys'