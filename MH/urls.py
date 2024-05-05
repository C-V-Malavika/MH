"""
URL configuration for MH project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("MH_App.urls")),
    path('home/', include("MH_App.urls")),
    path('signup/', include("MH_App.urls")),
    path('login/', include("MH_App.urls")),
    path('logout/', include("MH_App.urls")),
    path('profile/', include("MH_App.urls")),
    path('fill_profile/', include("MH_App.urls")),
    path('activity/', include("MH_App.urls")),
    path('view history/', include("MH_App.urls")),
    path('https://oviasree-blissbound-chatbot-app-zj10pk.streamlit.app/', include("MH_App.urls")),
    path('tasks/', include("MH_App.urls")),
]
