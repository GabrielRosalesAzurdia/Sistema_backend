from django.shortcuts import render
from rest_framework.response import Response # se utiliza response para enviar todos los datos y desenvocar en una vista de api
from rest_framework.decorators import api_view # api_view para que rest_framwork lo reconozca
from rest_framework import viewsets # viewsets para las vistas en clases
from django.utils.decorators import method_decorator # metodo para las clases
from .models import Grade, Class, Student, Score, Unit # modelos
from accounts.models import User # importamos al usuario
from . serializers import GradeSerializer, ClassSerializer, StudentSerializer, ScoreSerializer, UnitSerializer # serializers de los modelos de esta app
from django.views.decorators.cache import cache_page # cache
from django.shortcuts import get_object_or_404 # atajo para obtener un objeto o un error
from django.core import serializers # para deserializar los datos de request data
from django.http import HttpResponse

# @api_view(['GET'])
# def home(request):
#     current_user = User.objects.all()
#     return Response(current_user)

# view de los grados
class gradesView(viewsets.ViewSet):
    def list(self, request):
        current_user = request.user # recive el usuario
        queryset = Grade.objects.filter(teachers__pk=current_user.pk)
        serializer = GradeSerializer(queryset, many=True)
        return Response(serializer.data)

#view de las clases
class classesView(viewsets.ViewSet):
    def list(self, request):
        try: # añadiendo soporte para cuando getlist falle 
            grade = request.data.getlist('grade') # recibe ['x'] en postman
            current_user = request.user # recive el usuario
            queryset = Class.objects.filter(teachers__pk=current_user.pk).filter(grade__pk__in=grade) # filter(grades__pk__in=grades)  filter busca en una lista
            serializer = ClassSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response("Ha ocurrido un error")

#view de las unidades
class unitView(viewsets.ViewSet):
    def list(self,request):
        try:
            grade = request.data.getlist('grade') # recibe ['x'] en postman
            clase = request.data.getlist('clase') # recibe ['x'] en postman
            queryset = Unit.objects.filter(grade__pk__in=grade).filter(clase__pk__in=clase)
            serializer = UnitSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response("Ha ocurrido un error")

#view de los estudiantes
class studentView(viewsets.ViewSet):
    def list(self,request):
        try:
            grade = request.data.getlist('grade') # recibe ['x'] en postman
            clase = request.data.getlist('clase') # recibe ['x'] en postman
            queryset = Student.objects.filter(grade__pk__in=grade).filter(classes__pk__in=clase)
            serializer = StudentSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response("Ha ocurrido un error")

#view de las notas
class scoreView(viewsets.ViewSet):
    def list(self,request):
        try:
            #clase = request.data.getlist('clase') # recibe ['x'] en postman
            unit = request.data.getlist('unit') # recibe ['x'] en postman
            student = request.data.getlist('student') # recibe ['x'] en postman
            queryset = Score.objects.filter(unit__pk__in=unit).filter(student__pk__in=student)
            print(queryset)
            serializer = ScoreSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response("Ha ocurrido un error")

    def retrieve(self, request, pk=None):
        queryset = Score.objects.all()
        score = get_object_or_404(queryset, pk=pk)
        serializer = ScoreSerializer(score)
        return Response(serializer.data)