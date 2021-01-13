from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=130, required=True)
    subject = forms.CharField(label="Subject", max_length=130, required=True)
    email = forms.EmailField(label="Email", max_length=130, required=True)
    message = forms.CharField(label="Message", max_length=2000, required=True, widget=forms.Textarea)
