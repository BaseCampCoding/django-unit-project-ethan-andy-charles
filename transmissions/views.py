from django.views.generic import ListView, DetailView, CreateView
from .models import Transmission, Comment
from django.shortcuts import render
from django.conf import settings
from django.views.generic.edit import CreateView


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

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'transmission_new.html'
    fields = ('transmission', 'comment', 'author')

