from django.views.generic import ListView, DetailView
from .models import Transmission
from django.shortcuts import render
from django.conf import settings


class TransmissionListView(ListView):
    model = Transmission
    template_name = 'home.html'

class TransmissionDetailView(DetailView): 
    model = Transmission
    template_name = 'transmission_detail.html'

