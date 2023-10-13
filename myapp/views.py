from django.views import View
from django.shortcuts import render, redirect
from .models import CustomUser
from django.db import models

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.get(username=username, password=password)
            return redirect('home')
        except CustomUser.DoesNotExist:
            return redirect('register')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        CustomUser.objects.create(username=username, password=password)
        return redirect('login')


