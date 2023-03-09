from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from teacher.models import Teacher

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def index(request):
    return HttpResponse('this is common')

@api_view(['POST'])
def teacher_login(request):
    u_username=request.POST['username']
    p_password=request.POST['password']
    try:
        chek=Teacher.objects.get(username=u_username,password=p_password)
        status=True
    except:
        status=False
    return JsonResponse({'status':status})
   