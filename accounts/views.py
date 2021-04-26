from django.shortcuts import render
from rest_framework.response import Response # se utiliza response para enviar todos los datos y desenvocar en una vista de api
from rest_framework import viewsets # viewsets para las vistas en clases
from django.shortcuts import get_object_or_404 # atajo para obtener un objeto o un error
from .serializers import UserSerializer
from .models import User
from rest_framework.authtoken.views import ObtainAuthToken #clase para heredar 
from rest_framework.authtoken.models import Token # token en djangorestframework

#view de los usuarios
class usersView(viewsets.ViewSet):
    def list(self, request):
        current_user = request.user # recive el usuario
        serializer = UserSerializer(current_user)
        return Response(serializer.data)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_name':user.first_name,
            'email':user.email
        })