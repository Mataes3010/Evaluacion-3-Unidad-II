from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.landing_page, name='landing'),
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Rutas genéricas para listar, agregar, actualizar y eliminar registros
    path('<str:materia>/listar/', views.listar_registros, name='listar_registros'),
    path('<str:materia>/agregar/', views.agregar_registro, name='agregar_registro'),
    path('<str:materia>/actualizar/<int:pk>/', views.actualizar_registro, name='actualizar_registro'),
    path('<str:materia>/eliminar/<int:pk>/', views.eliminar_registro, name='eliminar_registro'),
]
