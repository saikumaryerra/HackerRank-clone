from django import forms

class codeForm(forms.Form):
   code = forms.CharField(widget=forms.Textarea(attrs={'rows': '16','cols':'102'}))