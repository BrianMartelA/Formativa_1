from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from .models import BoletaModel
from alumnos.models import Productos, proveedores





class SignUpForm(UserCreationForm):
    confirmarcorreo = forms.EmailField(label='confirmar correo')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id':'id_password1','type':'password'}))
    class Meta:
        model=User
        fields = ['username', 'password1', 'password2', 'email','confirmarcorreo']
        
    
    pass
    

class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'id_password1','type':'password'}))

    class Meta:
        model = User
        fields = ['email','password']

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
    
class BoletaForm(forms.ModelForm):

    class Meta:
        model = BoletaModel
        fields = ['desc_boleta','cant','precio']

# FORMULARIO PARA PRODUCTOS
class ProductosForm(forms.ModelForm):
    # ModelForm: Crea automáticamente un formulario basado en el modelo Productos
    # Genera campos, validaciones y funcionalidad save() automáticamente
    
    class Meta:
        # Clase interna que define la configuración del formulario
        
        model = Productos
        # Especifica que este formulario está basado en el modelo Productos
        
        fields = ['id','nombre', 'description', 'price', 'stock', 'categoria', 'image']
        # Lista de campos del modelo que se incluirán en el formulario
        # Solo estos campos aparecerán en el formulario renderizado
        
        labels ={
            # Diccionario que define las etiquetas personalizadas para cada campo
            'id' : 'ID',                    # Campo ID se mostrará como "ID"
            'nombre' : 'Nombre',            # Campo nombre se mostrará como "Nombre"
            'description': 'Descripción',   # Campo description se mostrará como "Descripción"
            'price': 'Precio',              # Campo price se mostrará como "Precio"
            'stock': 'Stock',               # Campo stock se mostrará como "Stock"
            'categoria':'Categoria',        # Campo categoria se mostrará como "Categoria"
            'image': 'Imagen',              # Campo image se mostrará como "Imagen"
        }
        
        widgets = {
            # Diccionario que define cómo se renderiza cada campo en HTML
            
            'id': forms.TextInput(
                # Campo ID como input de texto
                attrs={
                    'placeholder': 'Ingrese id...',     # Texto de ayuda dentro del campo
                    'id': 'id',                         # ID del elemento HTML
                    'class': 'form-control',           # Clase CSS Bootstrap
                }
            ),
            
            'nombre': forms.TextInput(
                # Campo nombre como input de texto
                attrs={
                    'placeholder': 'Ingrese nombre...',  # Texto de ayuda
                    'id': 'nombre',                      # ID del elemento HTML
                    'class': 'form-control',            # Clase CSS Bootstrap
                }
            ),
            
            'description': forms.TextInput(
                # Campo descripción como input de texto
                # SUGERENCIA: Debería ser Textarea para textos largos
                attrs={
                    'placeholder': 'Ingrese descripción...',  # Texto de ayuda
                    'id': 'description',                      # ID del elemento HTML
                    'class': 'form-control',                 # Clase CSS Bootstrap
                }
            ),
            
            'price': forms.NumberInput(
                # Campo precio como input numérico
                # Permite solo números y incluye controles de incremento/decremento
                attrs={
                    'placeholder': 'Ingrese precio...',  # Texto de ayuda
                    'id': 'price',                       # ID del elemento HTML
                    'class': 'form-control',            # Clase CSS Bootstrap
                }
            ),
            
            'stock': forms.NumberInput(
                # Campo stock como input numérico
                attrs={
                    'class': 'form-control',  # Clase CSS Bootstrap
                    'id': 'stock',            # ID del elemento HTML
                    # Nota: No tiene placeholder
                }
            ),
            
            'categoria': forms.Select(
                # Campo categoría como lista desplegable (dropdown)
                # Las opciones vienen del modelo/choices definidos en Productos
                attrs={
                    'id':'categoria',         # ID del elemento HTML
                    'class':'form-control',   # Clase CSS Bootstrap
                }
            ),
            
            'image': forms.FileInput(
                # Campo imagen como input de archivo
                # Permite seleccionar archivos desde el dispositivo
                attrs={
                    'class': 'form-control',  # Clase CSS Bootstrap
                    'id': 'image',            # ID del elemento HTML
                }
            )
        }
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = proveedores
        fields = ['nombre', 'description', 'numero', 'fecha_contrato']
        widgets = {'fecha_contrato':forms.DateInput(attrs={'type':'date'})}

