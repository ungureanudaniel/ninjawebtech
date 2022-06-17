from django import forms
from .models import Comment
from captcha.fields import CaptchaField

class CaptchaForm(forms.Form):
    captcha = CaptchaField()

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Your name"
        self.fields['text'].label = "Write your opinion here"
        self.fields['text'].widget.attrs.update({'class': 'comm_text'})
        self.fields['name'].widget.attrs.update({'class': 'comm_name'})
        self.fields['thumbnail'].label = "Add a photo of yourself"
        self.fields['thumbnail'].widget.attrs.update({'class': 'comm_img'})
        self.fields['name'].widget.attrs['style'] = "width:500px"
        self.fields['thumbnail'].widget.attrs['style'] = "width:500px"
        self.fields['text'].widget.attrs['style'] = "width:500px"
    class Meta:
        model=Comment
        fields=['name', 'text', 'thumbnail']
