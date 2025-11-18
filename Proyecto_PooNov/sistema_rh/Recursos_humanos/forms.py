from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Departamento, Cargo ,Contrato , Empleado , Asistencia,Usuario
from django.core.exceptions import ValidationError
import re



class RegistroForm(UserCreationForm):
    password1 = forms.CharField(label="Contrasena", widget=forms.PasswordInput,
                                help_text="Debe tener minimo 8 caracteres")
    password2 = forms.CharField(label="Confirmar contrasena", widget=forms.PasswordInput,
                                help_text="Confirme su contrasena")
    class Meta:
        model = Usuario
        fields = ['cedula', 'nombre', 'apellido', 'email', 'telefono', 'fecha_nacimiento',
                  'direccion', 'username', 'password1', 'password2' ]
        widgets = {'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})}

    def clean_cedula(self):
        cedula= self.cleaned_data.get('cedula')
        if not cedula.isdigit() or len(cedula)!=10:
            raise ValidationError("Debe agregar 10 digitos")

        provincia = int(cedula[0:2])
        if provincia <1 or provincia >24:
            raise ValidationError("Los digitos deben pertenecer a una provincia")

        digito_verificador = int(cedula[9])
        pares= sum(int(cedula[i]) for i in range (1,9,2))
        impares= 0
        for i in range(0,9,2):
            n = int(cedula[i])*2
            if n >9:
                n -=9
            impares += n
        total = pares + impares
        verificador_calculado = 10 - (total % 10) if (total % 10)!=0 else 0

        if verificador_calculado != digito_verificador:
            raise ValidationError("La cédula ecuatoriana no es válida.")

            # Validar unicidad
        if Usuario.objects.filter(cedula=cedula).exists():
            raise ValidationError("Esta cédula ya está registrada.")
        return cedula

    def clean_email(self):
        email =self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise ValidationError('Este correo ya esta registrado')
        return email

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono.isdigit() or len(telefono)!=10:
            raise ValidationError('El numero debe tener 10 digitos')

        if not telefono.startswith('09'):
            raise ValidationError('El número debe comenzar con 09, correspondiente a celulares en Ecuador.')
        return telefono

    def clean(self):
        clean_data = super().clean()
        password1 = clean_data.get("password1")
        password2 = clean_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError('Las contrasenas no coinciden')
        return clean_data









# --------- validador de cédula ecuatoriana ----------
def validacion_ced_ecuatoriana(cedula):
    if not cedula.isdigit() or len(cedula) != 10 :
        return False
    provincia = (cedula[0:2])

    if not (1 <= provincia <= 24 or provincia == 30):
      return False

    tercer= (cedula[2])
    if tercer >= 6:
        return False

    coef = [2,1,2,1,2,1,2,1,2]
    suma= 0
    for i in range(9):
        vali = (cedula[i]) * coef[i]
        if vali >= 10 :
            vali -= 9
        suma += vali
    mod = suma % 10
    verificador = 0 if mod == 0 else 10 - mod
    return verificador









class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre', 'descripcion']


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['nombre', 'salario_base']



class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['codigo', 'tipo', 'fecha_inicio', 'fecha_fin','detalles']

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'detalles': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['cedula','nombres','apellidos','correo','telefono', 'fecha_nacimiento', 'direccion','departamento','cargo','contrato','fecha_ingreso', 'activo']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type':'date'}),
            'fecha_ingreso': forms.DateInput(attrs={'type':'date'})
        }

    def validar_cedula(self):
        ced= self.cleaned_data['cedula'].strip()
        if not validacion_ced_ecuatoriana(ced):
            raise forms.ValidationError('cedula invalida')

        qs = Empleado.objects.filter(cedula=ced)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError('Cedula ya registrada')

        return ced


    def validar_nombres(self):
        nombres= self.cleaned_data['nombres'].strip()
        if len(nombres) == 0 :
            raise forms.ValidationError('El campo esta vacio')

        return nombres


    def validar_apellidos(self):
        apellidos=self.cleaned_data['apellidos'].strip()
        if len(apellidos) == 0 :
            raise forms.ValidationError('El campo esta vacio')
        return apellidos



class AsistenciaForm(forms.ModelForm):
   class Meta:
       model = Asistencia
       fields = ['empleado','fecha','hora_entrada','hora_salida', 'observaciones']

       widgets = {
           'empleado': forms.Select(attrs={'class': 'form-select'}),
           'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
           'hora_entrada': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
           'hora_salida': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
           'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
       }
