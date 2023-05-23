"""
URL configuration for djAfisha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/test/', views.director),
    path('api/v1/movie/', views.movies),
    path('api/v1/movie/<int:id>/', views.movies_detail),
    path('api/v1/review/',views.reviews ),
    path('api/v1/review/<int:id>/', views.reviews_detail),
    path('api/v1/director/', views.directors),
    path('api/v1/director/<int:id>/', views.directors_detail),
]
