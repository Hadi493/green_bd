from .models import Store
from django import forms

# Create your forms here.
class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'address', 'city', 'state', 'zip_code', 'store_profile']

    def __init__(self, *args, **kwargs):
        super(StoreForm, self).__init__(*args, **kwargs)
        self.fields['store_profile'].required = False