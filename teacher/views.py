from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TeacherSerializer

# here we import models(class)
from .models import Admin
from .models import Teacher

# Create your views here.
@api_view(['POST'])
def admin_login(request):
    u_username=request.POST['username']
    p_password=request.POST['password']
    try:
        chek=Admin.objects.get(username=u_username,password=p_password)
        status=True
    except:
        status=False
    return JsonResponse({'status':status})


@api_view(['POST'])
def add_teacher(request):
#    try:
#     params=request.data
#         serialised_data=TeacherSerializer(data=params)
#     if serialised_data.is_valid():
#             serialised_data.save()
#             return Response({'msg':'student added','status code':201})
#     else:
#         return Response({'msg':'form error','status code':403})
#     except:
#             return Response({'msg':'something went wrong......','status code':500})
        
   