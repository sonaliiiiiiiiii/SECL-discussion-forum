"""qna URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

admin.site.site_header = 'QNA Admin Panel'
admin.site.site_title = 'QNA Website'
admin.site.index_title = 'Welcome to QNA'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('questions/', include('questions.urls')),
    path('signup/', include('signup.urls')),
    path('logout/', views.logout, name='logout')
]

