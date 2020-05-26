from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('company_name', 'website', 'text', 'focus', 'based_in', 'made_in', 'low_price', 'high_price', 'tags')
