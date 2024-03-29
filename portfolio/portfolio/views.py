import requests
from project.models import Project
from project.models import ProjectImage
from project.models import TopicsLearnedList
from experience.models import Experience
from contact.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import send_mail
import json
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages


# Shows the homepage
def home(request):
    # Calls functions for each section in the homepage
    experiences = experience_section()
    projects = project_section()
    photos = project_images()
    topics = project_learned_topics()
    form = ContactForm()

    # Handles information from the contact form
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            captcha_token = request.POST.get("g-recaptcha-response")
            cap_url = "https://www.google.com/recaptcha/api/siteverify"
            cap_secret = settings.GOOGLE_RECAPTCHA_SECRET_KEY
            cap_data = {"secret": cap_secret, "response": captcha_token}
            cap_server_response = requests.post(url=cap_url, data=cap_data)
            result = json.loads(cap_server_response.text)
            if result['success']:
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
                messages.success(request, 'Your message was successfully sent!')
                return redirect('/#ContactMe')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                return redirect('/#ContactMe')

    # Renders all the subsections into the homepage template
    context = {'form': form, 'projects': projects, 'experiences': experiences, 'photos': photos, 'topics': topics}
    return render(request, '../templates/home_page.html', context)


# Creating the view for experience subsection
def experience_section():
    experiences = Experience.objects.order_by('year')
    return experiences


# Creating the view for the project section
def project_section():
    projects = Project.objects.order_by('year')
    return projects


# Loading images for all projects
def project_images():
    photos = ProjectImage.objects.all()
    return photos


# Returning learned topic list for all projects
def project_learned_topics():
    topics = TopicsLearnedList.objects.all()
    return topics


# Creating the view for the contact form section
def contact_section():
    form = ContactForm
    return form
