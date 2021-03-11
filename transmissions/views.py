from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Transmission, Comment
from django.shortcuts import render
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

class TransmissionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Transmission
    template_name = 'transmission_edit.html'
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TransmissionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Transmission
    template_name = 'transmission_delete.html'
    success_url =  reverse_lazy('home')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment_new.html'
    fields = ('transmission', 'comment', 'author')

class CommentUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Comment
    fields = ('comment')
    template_name = 'comment_edit'

class CommentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Comment
    template_name = 'comment_delete'
    success_url = reverse_lazy('transmission_detail')