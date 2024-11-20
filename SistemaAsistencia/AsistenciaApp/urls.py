from django.urls import path
from . import views

urlpatterns = [
    # Rutas para Aplicaciones Móviles Para IoT
    path('aplicaciones/', views.listar_aplicaciones_mobiles, name='listar_aplicaciones'),
    path('aplicaciones/agregar/', views.agregar_aplicaciones_mobiles, name='agregar_aplicaciones'),
    path('aplicaciones/eliminar/<int:pk>/', views.eliminar_aplicaciones_mobiles, name='eliminar_aplicaciones'),

    # Rutas para Ingeniería de Software
    path('ingenieria/', views.listar_ingenieria_software, name='listar_ingenieria'),
    path('ingenieria/agregar/', views.agregar_ingenieria_software, name='agregar_ingenieria'),
    path('ingenieria/eliminar/<int:pk>/', views.eliminar_ingenieria_software, name='eliminar_ingenieria'),

    # Rutas para Programación Back End
    path('programacion/', views.listar_programacion_backend, name='listar_programacion'),
    path('programacion/agregar/', views.agregar_programacion_backend, name='agregar_programacion'),
    path('programacion/eliminar/<int:pk>/', views.eliminar_programacion_backend, name='eliminar_programacion'),
]
