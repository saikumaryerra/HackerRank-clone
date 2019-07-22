from django import forms

class codeForm(forms.Form):
   code = forms.CharField(widget=forms.Textarea(attrs={'rows': '18','cols':'102'}))