from django.shortcuts import render
from django.http import HttpResponse

from teacher.models import Teacher
from teacher.serializer import TeacherSerializer

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
# @api_view(['POST'])
# def add_teacher(request):
#    try:
#         teacher_data=request.data
#         email_ex=Teacher.objects.filter(email=teacher_data['email']).exists()
#         if not email_ex:
#             serialised_data=TeacherSerializer(data= teacher_data)
#             if serialised_data.is_valid():
#                 serialised_data.save()
#                 return Response({'msg':'student added','status code':201})
#             else:
#                 return Response({'msg':'form error','status code':403})
#         else:
#             return Response({'msg':'e-mail already exist....'})
#     except Exception as d:
#         return Response({'msg':'something went wrong......','status code':500})
        

@api_view(['POST'])
def add_teacher(request):
    try:
        teacher_data = request.data
        # print(teacher_data,'ddddddddddd')
        email_ex = Teacher.objects.filter(username=teacher_data['username']).exists()
        if not email_ex:
            s_data = TeacherSerializer(data = teacher_data)
            if s_data.is_valid():
                s_data.save()
                msg = 'Teacher added'
            else:
                msg = 'From error'

        else:

            msg = 'E-mail already exist..'

    except Exception as d:
        print(d)
        msg = 'Something  wrong !!!'

    return JsonResponse({'msg':msg})


@api_view(['GET'])
def view_teacher(request):
    teacher_data=Teacher.objects.all()
    serialised_data=TeacherSerializer(teacher_data,many=True)
    return JsonResponse({'teacher': serialised_data.data})