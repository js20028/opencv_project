from django.urls import path

from . import views

app_name = 'FoodAllergy'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:allergy_id>/', views.detail, name='detail'),
    path('register/', views.allergy_register, name='register'),
    path('regist/', views.regist, name='regist'),
]