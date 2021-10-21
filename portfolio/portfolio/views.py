from django.shortcuts import render, get_object_or_404
from project.models import Project
from project.models import ProjectImage
from experience.models import Experience
from contact.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail


def landing(request):
    return render(request, '../templates/landing_page.html')


# Shows the homepage
def home(request):
    # Calls functions for each section in the homepage
    experiences = experience_section()
    projects = project_section()
    photos = project_images()
    form = ContactForm

    # Handles information from the contact form
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
            send_mail(str(subject), str(content),
                      settings.DEFAULT_FROM_EMAIL,
                      [
                          settings.EMAIL_HOST_USER,
                          'chin.portfolio.contact@gmail.com',
                      ])
            return HttpResponse('Thanks for contacting me!')

    # Renders all the subsections into the homepage template
    context = {'form': form, 'projects': projects, 'experiences': experiences, 'photos': photos}
    return render(request, '../templates/home_page.html', context)


# Creating the view for experience subsection
def experience_section():
    experiences = Experience.objects.order_by('year').reverse()
    return experiences


# Creating the view for the project section
def project_section():
    projects = Project.objects.order_by('year').reverse()
    return projects


# Loading images for all projects
def project_images():
    photos = ProjectImage.objects.all()
    return photos


# Creating the view for the contact form section
def contact_section():
    form = ContactForm
    return form

