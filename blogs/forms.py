from tinymce.widgets import TinyMCE
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'thumbnail']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget = forms.TextInput(attrs={
            'class': 'input-title',
            'placeholder': 'عنوان مقاله را وارد کنید...',
        })

        self.fields['content'].widget = forms.Textarea(attrs={
            'class': 'tinymce',
            'cols': 80,
            'rows': 30,
        })
        self.fields['content'].required = False
        self.fields['content'].label = 'محتوا'

        self.fields['thumbnail'].widget = forms.ClearableFileInput(attrs={
            'class': 'form-control',
        })
        self.fields['thumbnail'].label = 'تصویر مقاله'


class BlogAdminForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'content': TinyMCE(
                attrs={
                    'cols': 80,
                    'rows': 30,
                    'class': 'tinymce',
                }
            )
        }