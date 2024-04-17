from django import forms

from .models import Cars

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['brand', 'slug', 'color', 'photo', 'description',
                  'is_published', 'cat']

        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 47, 'rows': 5})
        }


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255,
                           widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-input'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}))
