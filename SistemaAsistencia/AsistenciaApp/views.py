from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import AplicacionesMóvilesParaIot, IngenieríaDeSoftware, ProgramaciónBackEnd

# Landing Page
def landing_page(request):
    """Página principal accesible sin autenticación"""
    return render(request, "landing_page/landing_page.html")

# Vistas para Aplicaciones Móviles Para IoT
@login_required
@permission_required('app.add_aplicacionesmóvilesparaiot', raise_exception=True)
def agregar_aplicaciones(request):
    if request.method == 'POST':
        horas = request.POST.get('horas_asistidas')
        fecha = request.POST.get('fecha_clase')
        AplicacionesMóvilesParaIot.objects.create(
            horas_asistidas=horas,
            alumno=request.user,
            fecha_clase=fecha
        )
        return redirect('listar_aplicaciones')
    return render(request, "aplicaciones/agregar.html")

@login_required
def listar_aplicaciones(request):
    registros = AplicacionesMóvilesParaIot.objects.all()
    return render(request, "aplicaciones/listar.html", {'registros': registros})

@login_required
@permission_required('app.change_aplicacionesmóvilesparaiot', raise_exception=True)
def actualizar_aplicaciones(request, pk):
    registro = get_object_or_404(AplicacionesMóvilesParaIot, pk=pk)
    if request.method == 'POST':
        registro.horas_asistidas = request.POST.get('horas_asistidas')
        registro.fecha_clase = request.POST.get('fecha_clase')
        registro.save()
        return redirect('listar_aplicaciones')
    return render(request, "aplicaciones/actualizar.html", {'registro': registro})

@login_required
@permission_required('app.delete_aplicacionesmóvilesparaiot', raise_exception=True)
def eliminar_aplicaciones(request, pk):
    registro = get_object_or_404(AplicacionesMóvilesParaIot, pk=pk)
    registro.delete()
    return redirect('listar_aplicaciones')

# Vistas para Ingeniería de Software
@login_required
@permission_required('app.add_ingenieríadesoftware', raise_exception=True)
def agregar_ingenieria(request):
    if request.method == 'POST':
        horas = request.POST.get('horas_asistidas')
        fecha = request.POST.get('fecha_clase')
        IngenieríaDeSoftware.objects.create(
            horas_asistidas=horas,
            alumno=request.user,
            fecha_clase=fecha
        )
        return redirect('listar_ingenieria')
    return render(request, "ingenieria/agregar.html")

@login_required
def listar_ingenieria(request):
    registros = IngenieríaDeSoftware.objects.all()
    return render(request, "ingenieria/listar.html", {'registros': registros})

@login_required
@permission_required('app.change_ingenieríadesoftware', raise_exception=True)
def actualizar_ingenieria(request, pk):
    registro = get_object_or_404(IngenieríaDeSoftware, pk=pk)
    if request.method == 'POST':
        registro.horas_asistidas = request.POST.get('horas_asistidas')
        registro.fecha_clase = request.POST.get('fecha_clase')
        registro.save()
        return redirect('listar_ingenieria')
    return render(request, "ingenieria/actualizar.html", {'registro': registro})

@login_required
@permission_required('app.delete_ingenieríadesoftware', raise_exception=True)
def eliminar_ingenieria(request, pk):
    registro = get_object_or_404(IngenieríaDeSoftware, pk=pk)
    registro.delete()
    return redirect('listar_ingenieria')

# Vistas para Programación Back End
@login_required
@permission_required('app.add_programaciónbackend', raise_exception=True)
def agregar_programacion(request):
    if request.method == 'POST':
        horas = request.POST.get('horas_asistidas')
        fecha = request.POST.get('fecha_clase')
        ProgramaciónBackEnd.objects.create(
            horas_asistidas=horas,
            alumno=request.user,
            fecha_clase=fecha
        )
        return redirect('listar_programacion')
    return render(request, "programacion/agregar.html")

@login_required
def listar_programacion(request):
    registros = ProgramaciónBackEnd.objects.all()
    return render(request, "programacion/listar.html", {'registros': registros})

@login_required
@permission_required('app.change_programaciónbackend', raise_exception=True)
def actualizar_programacion(request, pk):
    registro = get_object_or_404(ProgramaciónBackEnd, pk=pk)
    if request.method == 'POST':
        registro.horas_asistidas = request.POST.get('horas_asistidas')
        registro.fecha_clase = request.POST.get('fecha_clase')
        registro.save()
        return redirect('listar_programacion')
    return render(request, "programacion/actualizar.html", {'registro': registro})

@login_required
@permission_required('app.delete_programaciónbackend', raise_exception=True)
def eliminar_programacion(request, pk):
    registro = get_object_or_404(ProgramaciónBackEnd, pk=pk)
    registro.delete()
    return redirect('listar_programacion')
