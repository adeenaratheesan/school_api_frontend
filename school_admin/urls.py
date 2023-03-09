from django.urls import path
from .import views
urlpatterns=[
    path('admin_login',views.admin_login),
    path('add_teacher',views.add_teacher),
    path('view_teacher',views.view_teacher)

]