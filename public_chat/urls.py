from django.urls import path

from . import views

urlpatterns = [
    path('', views.live_chat_rooms, name="chat_rooms"),
]