from django.urls import path
<<<<<<< Updated upstream
<<<<<<< Updated upstream
from .views import TransmissionListView, TransmissionDetailView, TransmissionCreateView
=======
from .views import TransmissionListView, TransmissionDetailView, CommentCreateView
>>>>>>> Stashed changes
=======
from .views import TransmissionListView, TransmissionDetailView, CommentCreateView
>>>>>>> Stashed changes


urlpatterns = [
    path('Transmission/<int:pk>/', TransmissionDetailView.as_view(), name='transmission_detail'),
    path('new/', CommentCreateView.as_view(), name='transmission_new'),
    path('', TransmissionListView.as_view(), name='home'),
    path('transmission/new/', TransmissionCreateView.as_view(), name='transmission_new'),
]
