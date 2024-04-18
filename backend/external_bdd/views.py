from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import Group, User
from .models import ListaCarros

from rest_framework.permissions import IsAuthenticated  # permiso de autenticación de Django Rest Framework
from rest_framework.views import APIView  # clase base de vistas de la API de Django Rest Framework
from rest_framework.response import Response  # clase de respuesta de la API de Django Rest Framework
from rest_framework_simplejwt.authentication import JWTAuthentication  # Importa la autenticación JWT de Simple JWT

# vista de la API
