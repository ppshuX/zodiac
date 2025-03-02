"""
URL configuration for zodiac project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from stars import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aries/', views.aries, name='aries'),
    path('taurus/', views.taurus, name='taurus'),
    path('gemini/', views.gemini, name='gemini'),
    path('cancer/', views.cancer, name='cancer'),
    path('leo/', views.leo, name='leo'),
    path('virgo/', views.virgo, name='virgo'),
    path('libra/', views.libra, name='libra'),
    path('scorpio/', views.scorpio, name='scorpio'),
    path('sagittarius/', views.sagittarius, name='sagittarius'),
    path('capricornus/', views.capricornus, name='capricornus'),
    path('aquarius/', views.aquarius, name='aquarius'),
    path('pisces/', views.pisces, name='pisces'),
    path('admin/', admin.site.urls),
]
