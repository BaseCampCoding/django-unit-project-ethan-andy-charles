from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Transmission, Comment
from django.shortcuts import render
from django.conf import settings
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy

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