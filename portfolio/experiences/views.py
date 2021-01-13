from django.shortcuts import render
from .models import Experience


# Create your views here.
def experience_page(request):
    experiences = Experience.objects.order_by('start_date')
    return render(request, '../templates/experiences_page.html', {'experiences': experiences})
