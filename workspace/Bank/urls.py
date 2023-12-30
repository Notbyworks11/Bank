from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#urlconf
urlpatterns =[
    path("",views.home),
    path("home/",views.home),
    path("dashboard/",views.dashboard),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
