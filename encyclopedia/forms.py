from django import forms
 
 class ContentForm(forms.Form):
     title=forms.CharField(max_length=100,label="title")
     content=forms.CharField(widget=forms.Testarea)