from django.urls import path
from .import views  
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    
    path('', views.home, name="home"),
    path('create/', views.createMed, name="create_medicine"),
    path('update/<int:id>/', views.updateMed, name="update_medicine"),
    path('delete/<int:id>/', views.deleteMed, name="delete_medicine"),
    path('medicines/', views.listMed, name="list_medicine"),
    path('search/', csrf_exempt(views.search), name="search_medicine"),

]

