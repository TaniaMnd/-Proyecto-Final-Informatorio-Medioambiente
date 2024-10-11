from django import forms
from .models import Comentario

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