from django.urls import path
from .views import SignUpView, ShowProfilePageView, EditProfilePageView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    path('<int:pk>/edit/', EditProfilePageView.as_view(), name='edit_profile')
]

