from django.views.generic import CreateView
from .models import ContactForm


class ContactCreate(CreateView):
    model = ContactForm
    fields = ["first_name", "last_name", "subject", "message"]

