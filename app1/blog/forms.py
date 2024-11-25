from django import forms
from .models import Post,Comment,Category

choices = Category.objects.all().values_list('name','name')

c_list = []

for item in choices:
    c_list.append(item)
class PostForm(forms.ModelForm): 
    class Meta:
        model = Post
        fields = ['title', 'author' , 'category','body']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control','id':'author'}),
            'category': forms.Select(choices=c_list,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
        
        
        
class EditForm(forms.ModelForm): 
    class Meta:
        model = Post
        fields = ['title', 'body']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
        
class DateFilterForm(forms.Form):
    start_date = forms.DateField(widget=forms.SelectDateWidget, required=False)
    end_date = forms.DateField(widget=forms.SelectDateWidget, required=False)
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Write your comment here...', 'rows': 2}),
        }