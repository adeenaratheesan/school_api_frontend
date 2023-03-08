from django.urls import path
from .import views
urlpatterns=[
    path('add_teacher',views.add_teacher)
]