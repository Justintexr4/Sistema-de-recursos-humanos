from django.contrib import admin
from .models import Empleado,Contrato,Asistencia, Cargo,Departamento
# Register your models here.
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion')
    search_fields = ('Nombre',)

admin.site.register(Departamento,DepartamentoAdmin)


class CargoAdmin(admin.ModelAdmin):
    list_display= ('nombre','salario_base')
    search_fields = ('Nombre',)
admin.site.register(Cargo,CargoAdmin)


class ContratoAdmin(admin.ModelAdmin):
    list_display= ('codigo','tipo','fecha_inicio','fecha_fin','detalles')
    search_fields = ('codigo','tipo','fecha_inicio','fecha_fin','detalles')

admin.site.register(Contrato,ContratoAdmin)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display= ('cedula','nombres','apellidos','correo','telefono','fecha_nacimiento','direccion','departamento','cargo','contrato','fecha_ingreso','activo')
    search_fields = ('cedula','nombres','apellidos','correo')
admin.site.register(Empleado,EmpleadoAdmin)

class AsistenciaAdmin(admin.ModelAdmin):
    list_display= ('empleado','fecha','hora_entrada','hora_salida','observaciones')
    search_fields = ('empleado','fecha')

admin.site.register(Asistencia,AsistenciaAdmin)



