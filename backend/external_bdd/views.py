from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import Group, User
from .models import ListaCarros

from rest_framework.permissions import IsAuthenticated  # permiso de autenticación de Django Rest Framework
from rest_framework.views import APIView  # clase base de vistas de la API de Django Rest Framework
from rest_framework.response import Response  # clase de respuesta de la API de Django Rest Framework
from rest_framework_simplejwt.authentication import JWTAuthentication  # Importa la autenticación JWT de Simple JWT

# vista de la API

class get_vehiculos(APIView):
    # Utiliza el permiso de autenticación, solo los usuarios autenticados pueden acceder a esta vista
    permission_classes = [IsAuthenticated]  
    
    # Define las clases de autenticación que se aplicarán a la vista
    # Utiliza la autenticación JWT, lo que significa que los tokens JWT se utilizarán para autenticar a los usuarios
    authentication_classes = [JWTAuthentication]  
    
    def get(self, request):
        user = request.user
        print("Acceso correcto a la vista para: " + str(user))
        vehiculos = ListaCarros.objects.all()
        vehiculos_serializados = [{'name': vehiculo.name, 'description': vehiculo.description} for vehiculo in vehiculos]

        return JsonResponse({'vehiculos': vehiculos_serializados}, safe=False)

