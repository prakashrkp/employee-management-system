from django.urls import path
from . import views



urlpatterns = [
    path('', views.dashboard),
    path('dashboard/', views.dashboard),
    path('employees/',views.employee_list),
    path('add-employee/',views.add_employee),
    path('update/<int:id>/', views.update_employee),
    path('delete/<int:id>/', views.delete_employee),
    path('login/', views.user_login),
    path('logout/', views.user_logout),
   


]