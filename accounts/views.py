from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm


class ProfileView(TemplateView):
    template_name = 'profile_page.html'


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # salva i dati
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1'] #poiche abbiamo psw1 e psw2
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect('home')

    else:
        form = UserCreationForm()  # form non mandato in modo corretto

    return render(request, 'registration/register.html', {'form': form})
