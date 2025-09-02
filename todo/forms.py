from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    """
    Form for creating and editing Todo items.
    """
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }