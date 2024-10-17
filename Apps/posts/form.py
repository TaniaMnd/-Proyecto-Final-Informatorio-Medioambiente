from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Comentarios  # Asegúrate de que el modelo Comentarios esté importado
from django.contrib.auth.models import User
from .models import Posts


class RegistroForm(UserCreationForm):
    username = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre de usuario"},
        ),
    )
    email = forms.EmailField(
        max_length=200,
        help_text="Required",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "name@example.com"}
        ),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}), required=True
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}), required=True
    )
  
    icono = forms.ImageField(
        label="Imagen de perfil",
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control form-control-lg"}),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "icono"
        ]

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre de usuario"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Contraseña"}
        ),
        required=True
    )


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['titulo', 'contenido', 'imagen', 'categoria', 'autor']  # Asegúrate de incluir los campos que necesitas


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ['contenido']  # Cambia 'contenido' al nombre de tu campo
        widgets = {
            'contenido': forms.Textarea(attrs={'placeholder': 'Escribe tu comentario aquí...', 'class': 'form-control'}),
        }


class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
