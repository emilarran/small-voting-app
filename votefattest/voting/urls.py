from django.urls import path
from voting import views

urlpatterns = [
    path('', views.ListUsersView.as_view()),
    path('clap/<pk>/', views.ClapView.as_view()),
]