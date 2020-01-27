from django.shortcuts import render

from product import models

# Create your views here.
def index(request):
    productList =  models.Product.objects.all().filter(name="jithin")
    return render(request, 'product/home.html', { 'products' :productList })