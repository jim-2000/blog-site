from django import forms
from .models import article, author , comment, catagory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# create form hare 
class createForm(forms.ModelForm):
    class Meta:
        model = article
        fields = '__all__'
        exclude = [ 'article_author' ]
        
class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = [
           'first_name',
           'last_name',
           'email',
           'username',
           'password1',
           'password2'
          ]


class Public_author(forms.ModelForm):
    class Meta:
        model = author
        fields = [
           'profile_picture',
           'details'
        ]

        
class comment_form(forms.ModelForm):
    class Meta:
        model = comment
        fields = [
           'name',
           'email',
           'post_comment'
        ]
        
class Create_catagory(forms.ModelForm):
    class Meta:
        model = catagory
        fields = [
           'name',
           
        ]
        
        
        
        
        
        
        
        
        
        
             
        

