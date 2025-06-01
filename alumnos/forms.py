from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from .models import BoletaModel
from alumnos.models import Productos





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

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['id','nombre', 'description', 'price', 'stock', 'categoria', 'image']
        labels ={
            'id' : 'ID',
            'nombre' : 'Nombre',
            'description': 'Descripción',
            'price': 'Precio',
            'stock': 'Stock',
            'categoria':'Categoria',
            'image': 'Imagen',
        }
        widgets = {
            'id': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese id...',
                    'id': 'id',
                    'class': 'form-control',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre...',
                    'id': 'nombre',
                    'class': 'form-control',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese descripción...',
                    'id': 'description',
                    'class': 'form-control',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Ingrese precio...',
                    'id': 'price',
                    'class': 'form-control',
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'stock',
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'id':'categoria',
                    'class':'form-control',
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'image',
                }
            )
        }