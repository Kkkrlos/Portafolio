from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from .models import Project

def index(request):
    projects = Project.objects.all()

    return render(request, 'index.html', {'projects': projects})

def Linkedin(request):
    return redirect('https://www.linkedin.com/in/carlosrodriguez1205/')

def Github(request):
    return redirect('https://github.com/Kkkrlos')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        template = render_to_string('email/email_template.html', {
            'name': name,
            'email': email,
            'message': message
        })

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['rocarlos1205@gmail.com']
        )

        email.fail_silently = False
        email.send()
        messages.success(request, '¡Se ha enviado tu correo! :)')
        return redirect('contacto')

    return render(request, 'email/form.html')