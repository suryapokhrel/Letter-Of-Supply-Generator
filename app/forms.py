from django import forms
from .models import LOS  # Corrected import statement

class LOSForm(forms.ModelForm):
    specialSINs = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('[IT]', 'Information Technology'),
            ('[OFFICE]', 'Office Supplies'),
        ],
        required=False,
    )

    class Meta:
        model = LOS  # Use the correct model name
        fields = ['vendorName', 'vendorPOCName', 'vendorPOCTitle', 'vendorAddress', 'supplierName', 'supplierPOCName', 'supplierPOCTitle', 'supplierBrands', 'losType', 'contractNumber', 'specialSINs', 'letterhead']
