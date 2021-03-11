from django.views.generic import ListView, DetailView
from .models import Transmission
from django.shortcuts import render
from django.conf import settings
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class TransmissionListView(ListView):
    model = Transmission
    template_name = 'home.html'

class TransmissionDetailView(DetailView): 
    model = Transmission
    template_name = 'transmission_detail.html'

class TransmissionCreateView(LoginRequiredMixin, CreateView):
    model = Transmission
    template_name = 'transmission_new.html'
    fields = ['title', 'author', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
