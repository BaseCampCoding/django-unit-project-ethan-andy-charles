from django.urls import path
from .views import TransmissionListView, TransmissionDetailView


urlpatterns = [
    path('Transmission/<int:pk>/', TransmissionDetailView.as_view(), name='transmission_detail'),
    path('', TransmissionListView.as_view(), name='home'),
]
