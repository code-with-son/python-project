from django.shortcuts import render, redirect
from .models import Contact, UserRegister

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def sing(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        
        UserRegister.objects.create(
            name=name,
            email=email,
            phone=phone,
            password=password
        )

        return redirect('sing')   # lowercase

    return render(request, 'sing.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    message = ""

    if request.method == "POST":
        email = request.POST.get('email')
        if not Contact.objects.filter(email=email).exists():
            Contact.objects.create(
                email=email
            )
            message = "Subscribed Successfully ✅"
        else:
            message = "Email Already Exists ❌"

    return render(request, 'Contact.html', {"message": message})
