from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('path/',views.home,name="newhome"),
    path('deletetodo/<str:pk>',views.deletetodo,name="deletetodo"),
    path('updatetodo/<str:pk>',views.updatetodo,name="updatetodo"),
]
