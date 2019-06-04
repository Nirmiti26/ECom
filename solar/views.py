from django.shortcuts import render


def workstation(request):
    return render(request, 'solar/workstation.html')


def products(request):
    return render(request, 'solar/products.html')
