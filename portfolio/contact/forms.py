from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=130,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Name'})
    )
    subject = forms.CharField(
        label='',
        max_length=130,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Subject'})
    )
    email = forms.EmailField(
        label="",
        max_length=130,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
    message = forms.CharField(
        label="",
        max_length=2000,
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Message'})
    )
