from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import CustomUserCreationForm
from accounts.models import CustomUser

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# Create your views here.

class ShowProfilePageView(DetailView):
    model = CustomUser
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = CustomUser.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args , **kwargs)
        page_user = get_object_or_404(CustomUser, id=self.kwargs['pk'])
        context ['page_user'] = page_user 
        return context