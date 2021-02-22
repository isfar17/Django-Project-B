from django import forms
from django.forms import fields
from .models import Todo
 
class FormTodo(forms.ModelForm):

    class Meta():
        model=Todo
        fields="__all__"