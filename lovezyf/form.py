from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    name = forms.CharField(
        label= '',
        max_length=50,
        widget=forms.widgets.Input(
            attrs={'class': 'form-control',
                   'placeholder': '你的名字',
                   }
        )
    )
    content = forms.CharField(
        label="",
        max_length=300,
        widget=forms.widgets.Textarea(
            attrs={'rows': 6, 'cols': 60,
                   'class': 'form-control',
                   'placeholder': '请输入内容'}
        )
    )

    class Meta:
        model = Comment
        fields = ['name', 'content']