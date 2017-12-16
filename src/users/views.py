from django.contrib import messages
from django.contrib.auth import authenticate,login as django_login, logout as django_logout
from django.shortcuts import render, redirect
from django.views import View


class LoginView(View):

    def get(self,request):
        return render(request, "login_form.html")

    def post(self,request):
        username = request.POST.get("login_username")
        password = request.POST.get("login_password")
        # possible_usesr = User.objects.filter(username=username, password=password)  --> no lo puedo hacer asi porque la password hay que pasarla hasheada
        authenticate_user = authenticate(username=username, password=password)
        if authenticate_user and authenticate_user.is_active:
            django_login(request, authenticate_user)
            return redirect('home_page')
        else:
            messages.error(request, "Usuario incorrecto o inactivo")
            return render(request, "login_form.html")





def logout(request):
    django_logout(request)
    return redirect("login_page")
