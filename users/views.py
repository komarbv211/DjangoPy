from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .models import User

def register_view(request):
    if request.method == 'POST':
        username = request.POST['firstname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']

        if password != confirm_password:
            return render(request, 'users/register.html')
        
        hashed_password = make_password(password)

        user = User(username=username, email=email, password=hashed_password)
        user.save()

        print(f"Користувач зареєстрований: {user}")
        return render(request, "registration_success.html")

    return render(request, 'users/register.html')
