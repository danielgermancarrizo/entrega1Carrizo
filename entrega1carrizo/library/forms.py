from django import forms

class LibraryForm(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    birth_date = forms.DateTimeField()
    email = forms.EmailField() 
    tittle = forms.CharField()
    edition = forms.CharField()
    edition_date = forms.DateTimeField()    
    condition = forms.CharField()
    status = forms.CharField()
    avaible = forms.BooleanField()
    
