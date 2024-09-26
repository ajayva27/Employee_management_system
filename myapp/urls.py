from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.employee,name='employee'),
    path('', views.home, name='home'),
    path("add_employee",views.add_employee,name='add_employee'),
    path("delete_employee/<int:employee_id>/",views.delete_employee,name='delete_employee'),
    path("edit_employee/<int:employee_id>/", views.edit_employee, name='edit_employee'),
]