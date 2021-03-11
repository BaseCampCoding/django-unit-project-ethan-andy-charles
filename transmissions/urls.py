from django.urls import path

from .views import TransmissionListView, TransmissionDetailView, TransmissionCreateView, CommentCreateView



urlpatterns = [
    path('Transmission/<int:pk>/', TransmissionDetailView.as_view(), name='transmission_detail'),
    path('new/', CommentCreateView.as_view(), name='transmission_new'),
    path('', TransmissionListView.as_view(), name='home'),
    path('transmission/new/', TransmissionCreateView.as_view(), name='transmission_new'),
]
