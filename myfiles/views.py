import datetime

from django.shortcuts import render

# Create your views here.
from myfiles.models import *
def index(malumot):
    mobil = Mobiles.objects.all()
    audiosss = Audioss.objects.all()
    comp = Computers.objects.all()
    house = Household.objects.all()
    kitch = Kitchen.objects.all()
    news = Newproducts.objects.all()
    return render(malumot,'index.html',{'mobils':mobil,'audioss': audiosss,"comp":comp,'household':house,'kitchen':kitch,'news':news})

def products(malumot):
    mobil = Mobiles.objects.all()
    headp = Headphone.objects.all()
    m3 = mr3.objects.all()
    tegishli = Tegishli.objects.all()
    return render(malumot,'products.html',{'mobil': mobil,'head':headp,'mr3':m3,'tegishli':tegishli})

def products1(malumot):
    lap = Laptop.objects.all()
    desktop = Desktop.objects.all()
    wear = Wearable.objects.all()
    tegishli = Tegishli.objects.all()
    return render(malumot,'products1.html',{'laptop':lap,'desk':desktop,'wear':wear,'tegishli':tegishli})
def products2(malumot):
    tv = Tv.objects.all()
    camera = Camera.objects.all()
    grinder = Grinder.objects.all()
    tegishli = Tegishli.objects.all()
    return render(malumot,'products2.html',{'tv':tv,'camera':camera,'grinder':grinder,'tegishli':tegishli})
def single(malumot):
    return render(malumot,'single.html')
def mail(malumot):
    if malumot.method == "POST":
        name = malumot.POST.get('ism')
        email = malumot.POST.get('email')
        tel = malumot.POST.get('tel')
        text = malumot.POST.get('text')
        vaqt = datetime.datetime.now()
        murojaat(ism=name,email=email,tel=tel,murojat=text,vaqt=vaqt).save()
    return render(malumot,'mail.html')

def icons(malumot):
    return render(malumot,'icons.html')

def faq(malumot):
    return render(malumot,'faq.html')
def codes(malumot):
    return render(malumot,'codes.html')

def about(malumot):
    return render(malumot,'about.html')