from django import forms


class ShortUrlForm(forms.Form):
    url = forms.CharField(label="Long URL")
