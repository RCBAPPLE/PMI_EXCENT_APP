from django import forms
from .models import Diagnostic

class DiagnosticForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        lang = kwargs.pop('lang', 'FR')  # Par défaut, la langue est "FR"
        super().__init__(*args, **kwargs)

        # Définir les placeholders et labels dynamiquement selon la langue
        if lang == 'FR':
            self.fields['Client'].widget.attrs.update({
                'placeholder': 'ex : Airbus Blagnac',
                'class': 'custom-input'
            })
            self.fields['SN_JacXson'].widget.attrs.update({
                'placeholder': 'ex : SN01',
                'class': 'custom-input'
            })
            self.fields['Trigramme_Technicien'].widget.attrs.update({
                'placeholder': 'ex : 123',
                'class': 'custom-input'
            })
        elif lang == 'EN':
            self.fields['Client'].widget.attrs.update({
                'placeholder': 'e.g., Airbus Blagnac',
                'class': 'custom-input'
            })
            self.fields['SN_JacXson'].widget.attrs.update({
                'placeholder': 'e.g., SN01',
                'class': 'custom-input'
            })
            self.fields['Trigramme_Technicien'].widget.attrs.update({
                'placeholder': 'e.g., 123',
                'class': 'custom-input'
            })

    class Meta:
        model = Diagnostic
        fields = ['Client', 'SN_JacXson', 'Trigramme_Technicien']
