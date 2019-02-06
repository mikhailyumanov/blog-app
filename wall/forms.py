from django import forms


class PostForm(forms.Form):
    forms.CharField()
    your_name = forms.CharField(max_length=100)
    post_text = forms.CharField(widget=forms.Textarea, max_length=5000)
