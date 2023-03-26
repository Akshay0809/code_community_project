from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginPage , name="login"),

    path('logout/', views.logoutUser, name="logout"),

    path('register/', views.registerUser, name="register"),

    path('', views.HOME, name='home'),

    path('room/<str:pk>/', views.ROOM, name='room'),

    path('profile/<str:pk>', views.UserProfile , name='user-profile'),

    path('create-room/', views.createRoom , name='create-room'),

    path('update-room/<str:pk>', views.updateROOM, name='update-room'),

    path('delete-room/<str:pk>', views.deleteRoom, name='delete-room'),

    path('delete-message/<str:pk>', views.deleteMessage, name='delete-message'),


]
