from django.shortcuts import render, get_object_or_404
from project.models import Project
from project.models import ProjectImage
from experience.models import Experience
from contact.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.http import HttpResponse


def landing(request):
    return render(request, '../templates/landing_page.html')


# Shows the homepage
def home(request):
    # Calls functions for each section in the homepage
    experiences = experience_section()
    projects = project_section()
    # TODO: figure out how to past id from modal into here
    project = get_object_or_404(Project, id=3)
    photos = ProjectImage.objects.filter(project=project)
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
            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['chinzh00@gmail.com'],
                headers={'Reply to': email}
            )
            email.send()
            return HttpResponse('Thanks for contacting me!')

    # Renders all the subsections into the homepage template
    context = {'form': form, 'projects': projects, 'experiences': experiences, 'project': project, 'photos': photos}
    return render(request, '../templates/home_page.html', context)


# Creating the view for experience subsection
def experience_section():
    experiences = Experience.objects.order_by('year').reverse()
    return experiences


# Creating the view for the project section
def project_section():
    projects = Project.objects.order_by('year').reverse()
    return projects


# Creating the view for the contact form section
def contact_section():
    form = ContactForm
    return form

