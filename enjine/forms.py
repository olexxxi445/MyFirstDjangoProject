from django import forms
from enjine.models import Req


class ReqForm(forms.ModelForm):
	class Meta:
		model = Req
		fields = ('name', 'email', 'phone')