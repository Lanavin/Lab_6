from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import ListView
from .models import  *
# Create your views here.

def home(request):
    par = {
        'header': 'Home'
    }
    return render(request, 'home.html', context=par)


class ProductsView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products_list'

