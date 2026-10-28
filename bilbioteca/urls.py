from django.urls import path, include
from rest_framework import routers
from bilbioteca import views

enrutador = routers.DefaultRouter()

enrutador.register(r'paisesVS', views.PaisViewSet)
enrutador.register(r'regionesVS', views.RegionViewSet)
enrutador.register(r'provinciasVS', views.ProvinciaViewSet)
enrutador.register(r'comunasVS', views.ComunaViewSet)
enrutador.register(r'direccionesVS', views.DireccionViewSet)

urlpatterns = [
    path('', include(enrutador.urls)),
    path('regiones/listado_regiones', views.RegionListView.as_view()),
    path('paises/listado_paises', views.PaisListView.as_view()),
    path('bibliotecas/listado_bibliotecas', views.BibliotecaListView.as_view())
]