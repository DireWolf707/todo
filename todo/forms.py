from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title','memo','important',)
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Todo'}),
            'memo': forms.Textarea(
                attrs={'placeholder': 'Todo Description (optional)'}),
        }