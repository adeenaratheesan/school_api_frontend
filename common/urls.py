from django.urls import path
from .import views
urlpatterns=[
    path('index',views.index),
    path('teacher_login',views.teacher_login)

]