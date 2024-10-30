# urls.py
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.CreateRoom, name='create_room'),  # Use `create_room` to match the HTML form
    path('<str:room_name>/<str:username>/', views.MessageView, name='room'),  # Room view
]
