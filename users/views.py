from django.contrib.auth import  login
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
# Реєстрація
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")  
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {"form": form})

# Вхід
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  
        if form.is_valid():
            user = form.get_user()  
            login(request, user)  
            return redirect('posts:list')  
        else:
            form.add_error(None, 'Невірне ім’я користувача або пароль') 
    else:
        form = AuthenticationForm() 
    return render(request, 'users/login.html', {'form': form})
