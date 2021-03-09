from django.views.generic import ListView
from .models import Transmission


class TransmissionListView(ListView):
    model = Transmission
    template_name = 'home.html'
