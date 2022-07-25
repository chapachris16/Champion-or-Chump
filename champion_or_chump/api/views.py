from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .models import User
# from .sertializers import UserSerializer
# Create your views here.

@api_view(['Get'])
def getRoutes(request):
    return Response('Our API')

# @api_view(['GET'])
# def getUsers(request):
#     user = User.objects.all()
#     serializer = UserSerializer(user, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getUser(request):
#     user = User.objects.get(id=pk)
#     serializer = UserSerializer(user, many=False)
#     return Response(serializer.data)
