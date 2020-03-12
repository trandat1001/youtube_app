"""view_youtube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from videos import views

urlpatterns = [
    path('', views.index, name='video-index'),
    path('list/', views.index, name='video-list'),
    path('thumbs/<int:category_id>', views.thumbs, name='video-thumbs'),
    path('detail/<int:id>', views.detail, name='video-detail'),
    path('create/', views.create, name='video-create'),
    path('update/<int:id>', views.update, name='video-update'),
    path('delete/<int:id>', views.delete, name='video-delete'),
]
