from django import forms

SUBJECTS = (
    ('networking', 'Networking'),
    ('career', 'Career Opportunities'),
    ('questions', 'Questions'),
    ('comments', 'Comments/Suggestions'),
)


class ContactForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=130,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Name'})
    )
    subject = forms.ChoiceField(
        label='',
        choices=SUBJECTS,
        required=True,
        widget=forms.Select(attrs={'placeholder': 'Subject'})
    )
    email = forms.EmailField(
        label="",
        max_length=130,
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    message = forms.CharField(
        label="",
        max_length=2000,
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Message'})
    )
