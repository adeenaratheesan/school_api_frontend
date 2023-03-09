# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.

# from django.http import JsonResponse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

from django.http import JsonResponse
from school_admin.models import Admin
from .serializer import TeacherSerializer

# # here we import models(class)
# from .models import Admin
from .models import Teacher



# Create your views here.
# @api_view(['POST'])
# def teacher_login(request):
#     u_username=request.POST['username']
#     p_password=request.POST['password']
#     try:
#         chek=Teacher.objects.get(username=u_username,password=p_password)
#         status=True
#     except:
#         status=False
#     return JsonResponse({'status':status})






