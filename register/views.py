from django.shortcuts import render, redirect


# Create your views here.
def sign (request):
      return render(request, 'register/sign-up.html')


def log (request):
    return render(request, 'register/log-in.html')