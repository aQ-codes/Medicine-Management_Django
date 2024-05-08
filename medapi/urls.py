from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.signup, name="api-register"),
    path('login/', views.login, name="api-login"),
    path('create/', views.create, name="api-create"),
    path('update/<int:pk>', views.update, name="api-edit"),
    path('delete/<int:pk>', views.delete, name="api-delete"),
    path('list/', views.list, name="api-list"),
    
]