from django.urls import path
from .views import RoomView

urlpatterns = [
    path('home', RoomView.as_view()) #as_view converts RoomView in a view because it isnt
]