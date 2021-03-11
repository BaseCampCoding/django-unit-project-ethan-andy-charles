from django.urls import path
from .views import TransmissionListView, TransmissionDetailView, TransmissionCreateView, TransmissionUpdateView, TransmissionDeleteView


urlpatterns = [
    path('Transmission/<int:pk>/delete/', TransmissionDeleteView.as_view(), name='transmission_delete'),
    path('Transmission/<int:pk>/edit/', TransmissionUpdateView.as_view(), name='transmission_edit'),
    path('Transmission/<int:pk>/', TransmissionDetailView.as_view(), name='transmission_detail'),
    path('', TransmissionListView.as_view(), name='home'),
    path('transmission/new/', TransmissionCreateView.as_view(), name='transmission_new'),
]
