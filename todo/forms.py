from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title','description','important',)
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Todo'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Todo Description (optional)'}),
        }