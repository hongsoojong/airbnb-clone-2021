from django.views import View
from django.shortcuts import render
from . import forms


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm(initial={"email": "hsj@naver.com"})
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        return render(request, "users/login.html", {"form": form})
