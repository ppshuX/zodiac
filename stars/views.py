from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requests):
    return render(requests, 'index.html')

def aries(requests):
    return render(requests, 'aries.html')

def taurus(requests):
    return render(requests, 'taurus.html')

def gemini(requests):
    return render(requests, 'gemini.html')

def cancer(requests):
    return render(requests, 'cancer.html')

def leo(requests):
    return render(requests, 'leo.html')

def virgo(requests):
    return render(requests, 'virgo.html')

def libra(requests):
    return render(requests, 'libra.html')

def scorpio(requests):
    return render(requests, 'scorpio.html')

def sagittarius(requests):
    return render(requests, 'sagittarius.html')

def capricornus(requests):
    return render(requests, 'capricornus.html')

def aquarius(requests):
    return render(requests, 'aquarius.html')

def pisces(requests):
    return render(requests, 'pisces.html')
