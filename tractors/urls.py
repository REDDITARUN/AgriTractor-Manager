from django.urls import path, include
from . import views

urlpatterns = [
  path('signup/',views.SignupPage,name='signup'),
  path('login/',views.LoginPage,name='login'),
  path('', views.index, name='index'),
  path('<int:id>', views.view_tractor, name='view_tractor'),
  path('add/', views.add, name='add'),
  path('edit/<int:id>/', views.edit, name='edit'),
  path('delete/<int:id>/', views.delete, name='delete'),
  path('logout/',views.LogoutPage,name='logout'),
]