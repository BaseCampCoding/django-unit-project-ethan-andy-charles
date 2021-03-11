from django.urls import path

from .views import TransmissionListView, TransmissionDetailView, TransmissionCreateView,TransmissionDeleteView,TransmissionUpdateView, CommentCreateView, CommentUpdateView, CommentDeleteView



urlpatterns = [
    path('Transmission/<int:pk>/delete/', TransmissionDeleteView.as_view(), name='transmission_delete'),
    path('Transmission/<int:pk>/edit/', TransmissionUpdateView.as_view(), name='transmission_edit'),
    path('Transmission/<int:pk>/', TransmissionDetailView.as_view(), name='transmission_detail'),
    path('new/', CommentCreateView.as_view(), name='comment_new'),
    path('<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
    path('<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('', TransmissionListView.as_view(), name='home'),
    path('transmission/new/', TransmissionCreateView.as_view(), name='transmission_new'),

]