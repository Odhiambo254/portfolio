from django.shortcuts import render, redirect
from .models import Project
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')
def projects(request):
    return render(request, 'projects.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            f'message from {name}',
            name,
            message,
            [settings.DEFAULT_FROM_EMAIL], fail_silently=False
        )
        return redirect('home')
    return render(request, 'contact.html')