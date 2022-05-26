from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render

from .repositories.product_repo import ProductRepo

product_repo = ProductRepo()

def index(request):
    return render(request, 'index.html',
        {
         'products': product_repo.get_products(),
        }
    )


def login(request):
    return render(request, 'login.html')


def submit_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'pages/index.html')
    else:
        return render(request, 'pages/index.html')
