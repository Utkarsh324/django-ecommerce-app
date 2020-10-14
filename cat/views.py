from django.shortcuts import render
from django.http import HttpResponse
from .models import electronics
from .models import cloths
from .models import furnitures
from .models import vehical
from .models import camera


# Create your views here.

def ecat(request):
    watt = electronics.objects.all()
    results="electronics"   
    params={'catty':watt,'res':results}
    return render(request,'category.html',params)
def ccat(request):
    watt = cloths.objects.all()
    results="cloths"
        
    params={'catty':watt,'res':results}
    return render(request,'category.html',params)
def fcat(request):
    results="furnitures"
    watt = furnitures.objects.all()
    params={'catty':watt,'res':results}
    return render(request,'category.html',params)
def vcat(request):
    results="vehicals"
    watt = vehical.objects.all()
        
    params={'catty':watt,'res':results}
    return render(request,'category.html',params)
def pcat(request):
    results="cameras"
    watt = camera.objects.all()
        
    params={'catty':watt,'res':results}
    return render(request,'category.html',params)
