from django.shortcuts import render
from project.models import Project
from contact.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.http import HttpResponse


def landing(request):
    return render(request, '../templates/landing_page.html')


def home(request):
    projects = project_page()
    form = ContactForm

    if request.method == 'POST':
        form = form(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name', '')
            subject = request.POST.get('subject', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')

            template = get_template('../templates/contact_template.txt')
            context = {
                'name': name,
                'subject': subject,
                'email': email,
                'message': message,
            }
            content = template.render(context)
            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['chinzh00@gmail.com'],
                headers={'Reply to': email}
            )
            email.send()
            return HttpResponse('Thanks for contacting me!')

    context = {'form': form, 'projects': projects}
    return render(request, '../templates/home_page.html', context)


def project_page():
    projects = Project.objects.order_by('date')
    return projects


def contact():
    form = ContactForm
    return form


def project_by_title(request):
    projects = project_page()
    return render(request, '../templates/project_description.html', projects)



