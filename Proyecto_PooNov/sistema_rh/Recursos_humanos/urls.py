from django.urls import path
from . import views


app_name = 'Recursos_humanos'
urlpatterns = [


     #login y logout
     path("", views.login_registro_view, name='login_registro_view'),
     path("home/", views.home, name='home'),
     path("logout/", views.cerrar_sesion, name='cerrar_sesion'),
     #Enrutamiento de Departamento
     path("listar/departamento/", views.listar_departamento,name="listar_departamento"),
     path ("crear/departamento/", views.crear_departamento,name="crear_departamento"),
     path ("editar/departamento/<int:pk>/", views.editar_departamento ,name="editar_departamento"),

     path("eliminar/departamento/<int:pk>/",views.eliminar_departamento,name="eliminar_departamento"),

     #Enrutamiento de Contrato
     path ("listar/contrato/", views.listar_contrato,name="listar_contrato"),
     path ("crear/contrato/", views.crear_contrato,name="crear_contrato"),

     path ("editar/contrato/<int:pk>/", views.editar_contrato,name="editar_contrato"),

     path ("eliminar/contrato/<int:pk>/", views.eliminar_contrato,name="eliminar_contrato"),
     #enrutamiento de cargo
     path("listar/cargo", views.listar_cargo,name="listar_cargo"),
     path("crear/cargo", views.crear_cargo,name="crear_cargo"),
     path("editar/cargo/<int:pk>/", views.editar_cargo,name="editar_cargo"),
     path("eliminar/cargo/<int:pk>/", views.eliminar_cargo,name="eliminar_cargo"),
     #enrutamiento de empleado
     path("listar/empleado/", views.listar_empleado,name="listar_empleado"),
     path("crear/empleado/", views.crear_empleado,name="crear_empleado"),
     path("editar/empleado/<int:pk>/", views.editar_empleado,name="editar_empleado"),
     path("eliminar/empleado/<int:pk>/", views.eliminar_empleado,name="eliminar_empleado"),
     #enruntamiento asistencia
     path("listar/asistencia", views.listar_asistencia,name="listar_asistencia"),
     path("crear/asistencia", views.crear_asistencia,name="crear_asistencia"),
     path("editar/asistencia/<int:pk>/", views.editar_asistencia,name="editar_asistencia"),

     path("eliminar/asistencia/<int:pk>/",views.editar_asistencia,name="eliminar_asistencia"),

               ]