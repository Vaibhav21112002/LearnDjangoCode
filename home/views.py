from django.shortcuts import render
from home import models
from datetime import datetime
from django.contrib import messages
# Create your views here.


def index(request):
    dest1 = models.Destination()
    dest1.name = "vaibhav"
    dest1.img = "https://source.unsplash.com/1600x900/?ice,water"
    dest1.price = 45

    dest2 = models.Destination()
    dest2.name = "vaibhav Gutpa"
    dest2.img = "https://source.unsplash.com/1600x900/?fire,water"
    dest2.price = 450

    dest3 = models.Destination()
    dest3.name = "vaibhavG"
    dest3.img = "https://source.unsplash.com/1600x900/?hut,water"
    dest3.price = 4533


    dest4 = models.Destination()
    dest4.name = "Ishan Gupta"
    dest4.img = "https://source.unsplash.com/1600x900/?forest,water"
    dest4.price = 100

    dests = [dest1, dest2, dest3,dest4]
    return render(request, 'index.html', {'dests': dests})


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zipcode = request.POST.get('zipcode')
        contact = models.Contact(name=name, email=email, address=address,
                                 city=city, zipcode=zipcode, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message Has Been Submitted')
    return render(request, 'contact.html')
