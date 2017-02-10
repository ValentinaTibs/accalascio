from django.shortcuts import render
from django.utils.translation import activate


from datetime import datetime
import datetime as dt



from accalascio.models import *
from accalascio.forms import  BookingForm


def home(request):
    activate('en')
    return render(request, 'index2.html')

def contatti(request):
    return render(request, 'contatti.html')

def montagna(request):
    montagna_post = Post.objects.filter(cat = Category.objects.get(name='montagna'), active=True) 
    return render(request, 'montagna-attivita.html', {'all_post' : montagna_post})

def book(request,id_req):
    related_rent = Renting.objects.get(id = id_req) 

    removing_date = Booking.objects.filter(room = related_rent , start_date__gte = datetime.today()) 
    del_date =[]
    for elem in removing_date:
        giorni = elem.start_date
        while giorni <= elem.end_date:
            del_date.append(giorni.isoformat())
            giorni = giorni + dt.timedelta(days=int(1))

    def_data = { 'approved' : False , 'room': id_req}
    booking_form = BookingForm(request.POST or None,initial=def_data)
    if booking_form.is_valid():
        booking = booking_form.save(commit=False) 
        booking.room = related_rent
        booking.approved = False
        booking.save()
        return render(request, 'book.html', {'room' : related_rent,'form_done':True,'booking':booking})

    else:
        return render(request, 'book.html', {'room' : related_rent,'form':booking_form, 'del_date' : del_date})


def accalascio(request):
    camere = Renting.objects.filter(cat = catRent.objects.get(name='Camera'), active=True)
    bnb = Renting.objects.filter(cat = catRent.objects.get(name='BnB'), active=True)
    return render(request, 'accalascio.html', {'rooms' : camere , 'bnb':bnb})


def affitto(request):
    affitto_post = Post.objects.filter(cat = Category.objects.get(name='affitto'), active=True)
    return render(request, 'montagna-attrezzatura.html', {'all_post' : affitto_post})

def eventi(request):
    eventi_post = Post.objects.filter(cat = Category.objects.get(name='eventi'), active=True)
    return render(request, 'eventi.html', {'all_post' : eventi_post})

    
    