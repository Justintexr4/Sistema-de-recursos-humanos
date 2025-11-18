from django.contrib.auth.decorators import login_required
from django.contrib.sitemaps.views import index
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Recursos_humanos.forms import DepartamentoForm, ContratoForm, EmpleadoForm, CargoForm, AsistenciaForm,RegistroForm
from Recursos_humanos.models import Departamento, Contrato, Empleado, Cargo, Asistencia


# Create your views here.


#Login


def login_registro_view(request):
    form = RegistroForm()
    mostrar_registro = False  # Estado por defecto (mostrar login)

    # Si se envió el formulario de registro
    if request.method == 'POST' and 'cedula' in request.POST:
        form = RegistroForm(request.POST)
        mostrar_registro = True
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado correctamente.')
            return redirect('Recursos_humanos:login_registro_view')  # Regresa al login tras registrar

    #  Si se envió el formulario de login
    elif request.method == 'POST' and 'username' in request.POST and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Recursos_humanos:home')  # redirige a tu inicio
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
            return redirect('Recursos_humanos:login_registro_view')


    return render(request, 'account/login_registro.html', {
        'form': form,
        'mostrar_registro': mostrar_registro
    })

#Departamentoviews
@login_required
def home(request):
    return render(request,'index/home.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('Recursos_humanos:login_registro_view')

def listar_departamento(request):
    departamentos = Departamento.objects.all()

    return render(request,"departamento/listar.html",{'departamentos':departamentos})


def crear_departamento(request):
    form = DepartamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("Recursos_humanos:listar_departamento")

    return render(request,"departamento/crear.html",{'form':form})


def editar_departamento(request,pk):
    departamentos = get_object_or_404(Departamento, pk=pk)

    form = DepartamentoForm(request.POST or None , instance=departamentos)

    if form.is_valid():
        form.save()
        return redirect("Recursos_humanos:listar_departamento")

    return render(request,"departamento/editar.html",{'form':form,'departamentos':departamentos})

def eliminar_departamento(request,pk):
    departamentos = get_object_or_404(Departamento, pk=pk)
    if request.method == 'POST':
        departamentos.delete()
        return redirect("Recursos_humanos:listar_departamento")

    return render(request,"departamento/eliminar.html",{'departamentos':departamentos})


#Contrato views


def listar_contrato(request):
    contratos = Contrato.objects.all()
    return render(request,"contrato/listar.html",{'contratos':contratos})

def crear_contrato(request):
    form = ContratoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("Recursos_humanos:listar_contrato")
    return render(request,"contrato/crear.html",{'form':form})


def editar_contrato(request,pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    form = ContratoForm(request.POST or None , instance=contrato)

    if form.is_valid():
        form.save()
        return redirect("Recursos_humanos:listar_contrato")

    return render(request,"contrato/editar.html",{'form':form,'contrato':contrato})



def eliminar_contrato(request,pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    if request.method == 'POST':
        contrato.delete()
        return redirect("Recursos_humanos:listar_contrato")
    return render(request,"contrato/eliminar.html",{'contrato':contrato})

#views de Cargo


def listar_cargo(request):
    cargos = Cargo.objects.all()
    return render(request,"cargo/listar.html",{'cargos':cargos})

def crear_cargo(request):
    form = CargoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("Recursos_humanos:listar_cargo")

    return render(request,"cargo/crear.html",{'form':form})
def editar_cargo(request,pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    form = CargoForm(request.POST or None , instance=cargo)
    if form.is_valid():
        form.save()
        return redirect("Recursos_humanos:listar_cargo")

    return render(request,"cargo/editar.html",{'form':form,'cargo':cargo})

def eliminar_cargo(request,pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    if request.method == 'POST':
        cargo.delete()
        return redirect("Recursos_humanos:listar_cargo")
    return render(request,"cargo/eliminar.html",{'cargo':cargo})
#views de Empleado

def listar_empleado(request):
    empleados = Empleado.objects.all()
    return  render(request,"empleado/listar.html",{'empleados':empleados})
def crear_empleado(request):
    form = EmpleadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("Recursos_humanos:listar_empleado")
    return render(request,"empleado/crear.html",{'form':form})


def editar_empleado(request,pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    form = EmpleadoForm(request.POST or None , instance=empleado)
    if form.is_valid():
        form.save()

        return redirect("Recursos_humanos:listar_empleado")

    return render(request,"empleado/editar.html",{'form':form,'empleado':empleado})


def eliminar_empleado(request,pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect("Recursos_humanos:listar_empleado")

    return render(request,"empleado/eliminar.html",{'form':empleado})

#views Asistencia

def listar_asistencia(request):
    asistencias = Asistencia.objects.all()

    return render(request,"asistencia/listar.html", {'asistencias':asistencias})


def crear_asistencia(request):
    form = AsistenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("Recursos_humanos:listar_asistencia")

    return render(request,"asistencia/crear.html",{'form':form})


def editar_asistencia(request,pk):
    asistencia = get_object_or_404(Asistencia, pk=pk)
    form = AsistenciaForm(request.POST or None , instance=asistencia)

    if form.is_valid():
        form.save()
        return redirect("Recursos_humanos:listar_asistencia")

    return render(request,"asistencia/editar.html",{'form':form})




def eliminar_asistencia(request,pk):
    asistencia = get_object_or_404(Asistencia, pk=pk)
    if request.method == 'POST':
        asistencia.delete()

        return redirect("Recursos_humanos:listar_asistencia")
    return render(request,"asistencia/eliminar.html",{'form':asistencia})
