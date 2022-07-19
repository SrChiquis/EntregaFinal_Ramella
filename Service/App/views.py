from distutils.log import info
from email.message import EmailMessage
import re
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.urls import reverse
# from App.forms import UserRregisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ContactForm

from App.forms import ContactForm
# Create your views here.

def inicio(request):
    return render(request, "App/home.html")

def faq(request):
    return render(request,"App/faq.html")


def contacto(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            email = EmailMessage(
                "ChiquiServis: Nuevo mensaje de consulta",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["srchiquis@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                return redirect(reverse('Contacto')+"?ok")
            except:
                return redirect(reverse('Contacto')+"?fail")
    
    return render(request, "App/contact.html",{'form':contact_form})

def about(request):
    return render(request, "App/about.html")

def blog(request):
    return render(request, "App/blog.html")

    