from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Sum
from .models import AplicacionesMóvilesParaIot, IngenieríaDeSoftware, ProgramaciónBackEnd

# Landing Page
def landing_page(request):
    """Página principal accesible sin autenticación"""
    return render(request, "landing_page/landing_page.html")

# Dashboard
@login_required
def dashboard(request):
    """Vista principal del sistema después de iniciar sesión"""
    return render(request, "base/dashboard.html")

# Listar registros
@login_required
def listar_registros(request, materia):
    """Vista para listar registros dinámicamente según la materia"""
    modelos = {
        'aplicaciones': AplicacionesMóvilesParaIot,
        'ingenieria': IngenieríaDeSoftware,
        'programacion': ProgramaciónBackEnd
    }
    
    if materia not in modelos:
        return render(request, "404.html")  # Página 404 si la materia no existe
    
    modelo = modelos[materia]
    registros = modelo.objects.all()
    suma_horas = modelo.objects.aggregate(total_horas_asistidas=Sum('horas_asistidas'))['total_horas_asistidas'] or 0
    
    return render(request, "base/listar.html", {
        'registros': registros,
        'materia': materia,
        'suma_horas': suma_horas
    })

# Agregar registro
@login_required
@permission_required('AsistenciaApp.add_aplicacionesmóvilesparaiot', raise_exception=True)
def agregar_registro(request, materia):
    """Vista para agregar un registro en una materia específica"""
    modelos = {
        'aplicaciones': AplicacionesMóvilesParaIot,
        'ingenieria': IngenieríaDeSoftware,
        'programacion': ProgramaciónBackEnd,
    }
    
    if materia not in modelos:
        return render(request, "404.html")
    
    modelo = modelos[materia]
    
    if request.method == 'POST':
        horas = request.POST.get('horas_asistidas')
        fecha = request.POST.get('fecha_clase')
        modelo.objects.create(
            horas_asistidas=horas,
            alumno=request.user,
            fecha_clase=fecha
        )
        return redirect('listar_registros', materia=materia)
    
    return render(request, "base/AgregarRegistro.html", {'materia': materia})

# Actualizar registro
@login_required
@permission_required('AsistenciaApp.change_aplicacionesmóvilesparaiot', raise_exception=True)
def actualizar_registro(request, materia, pk):
    """Vista para actualizar un registro en una materia específica"""
    modelos = {
        'aplicaciones': AplicacionesMóvilesParaIot,
        'ingenieria': IngenieríaDeSoftware,
        'programacion': ProgramaciónBackEnd,
    }
    
    if materia not in modelos:
        return render(request, "404.html")
    
    modelo = modelos[materia]
    registro = get_object_or_404(modelo, pk=pk)
    
    if request.method == 'POST':
        registro.horas_asistidas = request.POST.get('horas_asistidas')
        registro.fecha_clase = request.POST.get('fecha_clase')
        registro.save()
        return redirect('listar_registros', materia=materia)
    
    return render(request, "base/editar.html", {'registro': registro, 'materia': materia})

# Eliminar registro
@login_required
@permission_required('AsistenciaApp.delete_aplicacionesmóvilesparaiot', raise_exception=True)
def eliminar_registro(request, materia, pk):
    """Vista para eliminar un registro en una materia específica"""
    modelos = {
        'aplicaciones': AplicacionesMóvilesParaIot,
        'ingenieria': IngenieríaDeSoftware,
        'programacion': ProgramaciónBackEnd,
    }
    
    if materia not in modelos:
        return render(request, "404.html")
    
    modelo = modelos[materia]
    registro = get_object_or_404(modelo, pk=pk)
    registro.delete()
    return redirect('listar_registros', materia=materia)
