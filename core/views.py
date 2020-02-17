from django.shortcuts import render
from .models import Item


def index(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'index.html', context)


def product(request):
    return render(request, "product.html")


def about(request):
    return render(request, "about.html")
