from django.shortcuts import render
from rest_framework.response import Response # se utiliza response para enviar todos los datos y desenvocar en una vista de api
from rest_framework import viewsets # viewsets para las vistas en clases
from django.shortcuts import get_object_or_404 # atajo para obtener un objeto o un error
from .serializers import UserSerializer
from .models import User

#view de los usuarios
class usersView(viewsets.ViewSet):
    def list(self, request):
        current_user = request.user # recive el usuario
        serializer = UserSerializer(current_user)
        return Response(serializer.data)