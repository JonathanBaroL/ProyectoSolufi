from django.shortcuts import render
from django.contrib.auth import authenticate, login

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.decorators import api_view
from rest_framework.response import Response


from django.middleware.csrf import get_token
from django.http import JsonResponse

from django.contrib.auth.models import User #Sirve para traer informacion del usuario



# - Este metodo regresa el token middleware que ayuda a proteger la app de ataques CSRF
def csrf_token_view(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})


class IniciarSesion(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [AllowAny]  #Permite el acceso a usuarios no logeados (por ser un login)

    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username)
        print(str(password))
        user = authenticate(request, username=username, password=password) #Este metodo verifica las credenciales, NO SE LOGEA!!

        user_data = {
            'grup' : "",
            'user' : "",
            'message' : "Contraseña y/o usuario incorrectos",
            'session' : False
        }
        if user is not None:   #Si las credenciales son correctas entra
            nombre_grupo = ""
            usuario = User.objects.get(username = username)   #Recupera el nombre de usuario
            
            # los grupos a los que pertenece el usuario
            grupo = usuario.groups.all()     #regresa el o los grupos al que pertenece el usuario
            for grup in grupo:
                nombre_grupo = grup.name
            login(request, user)     #Este metodo, SI SE LOGEA 
            
            msg = 'Inicio de sesión exitoso, grupo: {}'.format(str(nombre_grupo))
            user_data = {
                'group' : nombre_grupo,
                'user' : username,
                'message' : msg,
                'session' : True
            }
            
            # Generar un token de acceso para el usuario
            access_token = AccessToken.for_user(usuario)
            print("TOKEN: " + str(access_token))
            response_data = {
                'user': user_data,
                'access_token': str(access_token),  # Convertimos el token a una cadena antes de devolverlo
                'status': 'ok'
            }

            
            return JsonResponse(response_data)
        else:
            print("Contraseña y/o usuario incorrectos")
            response_data = {
                'user': "NA",
                'access_token': "NA",  # Convertimos el token a una cadena antes de devolverlo
                'status': 'error',
                'mensaje':'Contraseña y/o usuario incorrectos'
            }
            return JsonResponse(response_data)



def index(request):
    return render(request, 'index.html')

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    lastname = request.data.get('cellphone')
    
    # Crea un nuevo usuario
    user = User.objects.create_user(username=username, email=email, password=password, last_name=lastname, is_active=True, is_staff=True)
    
    return Response({'message': 'Usuario creado exitosamente'})