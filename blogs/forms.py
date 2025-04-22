from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'excerpt', 'image', 'status']
        widgets = {
            'content': forms.Textarea(attrs={'style': 'display:none;'}),
            'excerpt': forms.Textarea(attrs={'rows': 3}),
            'status': forms.Select(choices=Blog.STATUS_CHOICES),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 10:
            raise forms.ValidationError("عنوان باید حداقل ۱۰ کاراکتر باشد")
        return title

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].required = False