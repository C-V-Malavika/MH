from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('signup/', views.signup, name = "signup"),
    path('login/', views.login, name = "login"),
    path('logout/', views.logout, name = "logout"),
    path('profile/', views.profile, name = "profile"),
    path('fill_profile/', views.fill_profile, name = "fill_profile"),
    path('activity/', views.activity, name = "activity"),
    path('view history/', views.view_history, name = "view history"),
    path('chat with bot/', views.chatbot, name = "chatbot"),
    path('tasks/', views.tasks, name = "tasks"),
]