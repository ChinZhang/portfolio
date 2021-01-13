from django.views.generic import CreateView
from .models import ContactForm
from django.urls import reverse_lazy
from django.http import HttpResponse


class ContactCreate(CreateView):
    model = ContactForm
    fields = ["first_name", "last_name", "subject", "message"]
    success_url = reverse_lazy("thanks")


def thanks(request):
    return HttpResponse("Thank you! Will get in touch soon.")
