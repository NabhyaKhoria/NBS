from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.models import User, auth
# Create your views here.
def hello(request):
    return render(request, 'home.html')

def buy(request):
    items = Product.objects.all()
    return render(request, 'buy.html', {'items': items})

def sell(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        description = request.POST.get('description')
        category = request.POST.get('category')
        price = request.POST.get('price')
        img = request.POST.get('file')
        item = Product(name=name, description=description, category=category, price=price, img=img)
        item.save()
        print('ITEM CREATED DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD')
        return redirect('buy')
        
    else:
        return render(request, 'sell.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
