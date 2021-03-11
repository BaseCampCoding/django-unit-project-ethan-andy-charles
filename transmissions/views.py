from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Transmission, Comment
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect

def LikeView(request, pk):
    transmission = get_object_or_404(Transmission, id=request.POST.get('transmission_id'))
    transmission.likes.add(request.user)
    return HttpResponseRedirect(reverse('transmission_detail', args=[str(pk)]))
    



class TransmissionListView(ListView):
    model = Transmission
    template_name = 'home.html'

class TransmissionDetailView(DetailView): 
    model = Transmission
    template_name = 'transmission_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TransmissionDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Transmission, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        return context


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
    fields = ('comment',)
    template_name = 'comment_edit.html'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CommentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

