from django.urls import path
from . import views
app_name = 'signup'
urlpatterns = [
    path('', views.signup, name='signup'),
    path('account', views.signup, name='account'),
    path('logout', views.logout, name='logout')
]
