from rest_framework import routers
from . import views
from django.urls import path,include

router = routers.DefaultRouter()

router.register('miusuarios',views.MiUsuarioViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('login/', views.ObtenerToken.as_view(),name='token-auth')
]