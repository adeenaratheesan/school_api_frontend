from django.shortcuts import render
from django.http import HttpResponse

from .models import Admin
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .serializer import AdminSerializers

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