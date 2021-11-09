from django.urls import path

from . import views

app_name = 'FoodAllergy'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:allergy_id>/', views.detail, name='detail'),
    path('register/', views.allergy_register, name='register'),
    path('regist/', views.regist, name='regist'),
    path('register/<str:allergy_name>/', views.showLv2, name='showLv2'),
    path('register/myAllergy/<str:allergy_name>/', views.myShowLv2, name='myShowLv2'),
    path('register/addMyAllergy', views.addMyAllergy, name='addMyAllergy'),
    path('register/deleteMyAllergy', views.deleteMyAllergy, name='deleteMyAllergy'),
]