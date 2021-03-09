from django.urls import path
from .views import TransmissionListView


urlpatterns = [
    path('', TransmissionListView.as_view(), name='home'),
]
