from django.views.generic import ListView, DetailView
from .models import Transmission
from django.shortcuts import render
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class TransmissionListView(ListView):
    model = Transmission
    template_name = 'home.html'

class TransmissionDetailView(DetailView): 
    model = Transmission
    template_name = 'transmission_detail.html'

class TransmissionCreateView(CreateView):
    model = Transmission
    template_name = 'transmission_new.html'
    fields = ['title', 'author', 'body']

class TransmissionUpdateView(UpdateView):
    model = Transmission
    template_name = 'transmission_edit.html'
    fields = ['title', 'body']

class TransmissionDeleteView(DeleteView):
    model = Transmission
    template_name = 'transmission_delete.html'
    success_url =  reverse_lazy('home')
