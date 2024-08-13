from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.help_text = ""

        self.fields['username'].widget.attrs.update({
            'class':"form-control my-2",
            'placeholder':'Kullanıcı adı...'
        })

        self.fields['email'].widget.attrs.update({
            'class':"form-control my-2",
            'placeholder':'email adresi...'
        })

        self.fields['password1'].widget.attrs.update({
            'class':"form-control my-2",
            'placeholder':'parola...'
        })

        self.fields['password2'].widget.attrs.update({
            'class':"form-control my-2",
            'placeholder':'Parola tekrar...'
        })