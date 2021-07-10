from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=email, first_name=first_name, email=email, password=password)
        user.save()
        print('user created')
        return redirect('/')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            print('Logged in user')
            auth.login(request, user)
            return redirect('/access/hello')
    else:
        return render(request, 'login.html')
        