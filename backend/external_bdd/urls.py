from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('api/get-vehiculos/', views.get_vehiculos.as_view(), name='get_vehiculos'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),            #
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),           # URLS para acceso a la verificacion del token
]