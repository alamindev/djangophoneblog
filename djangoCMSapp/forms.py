from django import forms
from tinymce import TinyMCE
from .models import Post,Comment,About,Contect
from django.contrib.auth import get_user_model
User = get_user_model()

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'overview', 'content', 'thumbnail', 
        'category', 'featured', 'previous_post', 'next_post')
class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Type Your Comment',
        'id':'usercomment',
        'rows':'4',

    }))
    class Meta:
        model = Comment
        fields = ('content',)
                    
class registerForm(forms.ModelForm):
    email = forms.EmailField(label="Enter your email")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Same Password", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email')
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password do not match')
        return password2
    def save(self, commit=True):
        user = super(registerForm, self).save(commit= False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('Name','Email','profile_picture')
class ContectForm(forms.ModelForm):
    class Meta:
        model =  Contect
        fields = ('Name','Email','Messages')                 

