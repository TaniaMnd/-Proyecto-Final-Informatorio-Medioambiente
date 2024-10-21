from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  
from .models import Comentario, Post

#Formulario COMENTARIOS EN NOTICIAS
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido'] 
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contenido'].widget.attrs.update({
            'placeholder': 'Escribe tu comentario..',
            'rows': '1',
            'class': 'form-control'  
        })


#Formulario de registro
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
            "icono",
        ]
                

#Formulario LOGIN
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

    
#Formulario contacto

class ContactForm(forms.Form):
    nombre_apellido = forms.CharField(max_length=100, widget=forms.TextInput)
    asunto = forms.CharField(widget=forms.Textarea) 
    comentario = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(widget=forms.EmailInput)    
    telefono = forms.CharField(max_length=15, widget=forms.TextInput)
      
      
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'resumen', 'texto', 'imagen', 'categoria'] 
      