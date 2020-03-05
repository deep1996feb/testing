from django import forms
from demo1.models import Truth
class MyForm(forms.ModelForm):
	class Meta:
		model=Truth
		fields=['name','mobile','salary','email']