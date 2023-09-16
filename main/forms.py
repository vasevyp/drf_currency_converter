from django import forms


class VolumeForm(forms.Form):
    volume_form = forms.FloatField(label='Currency volume', initial=1)
