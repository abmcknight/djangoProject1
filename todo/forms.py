from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

        widgets = {
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add tasks'
            }),
            'completed': forms.CheckboxInput(attrs={
                'style': 'width:20px;height:20px;'})
        }
