from django.urls import path
from .views import LegoToyListView

urlpatterns = [
    path('', LegoToyListView.as_view(), name='lego-toys'), 
]