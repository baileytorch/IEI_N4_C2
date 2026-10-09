from django.contrib import admin
from django.urls import path,include
from bilbioteca import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio),
    path('bilbioteca/',include('bilbioteca.urls'))
]
