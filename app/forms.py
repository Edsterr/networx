from django import forms
from app.models import User

class ModelForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['sid', 'name', 'location', 'floor']