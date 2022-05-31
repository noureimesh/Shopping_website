import os

from django.contrib.auth import authenticate, logout,login
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .forms import LoginForm
from .repositories.product_repo import ProductRepo

product_repo = ProductRepo()


@login_required(login_url="/login")
def index(request):
    current_user = request.user
    products = product_repo.get_products()
    for product in products:
        product.photo = os.path.basename(product.photo.path)

    return render(request, 'index.html',
                  {
                      'products': products,
                      'user_id': current_user.id,
                      'total_cart': product_repo.get_total_products(request.user),

                  }
                  )


@login_required(login_url="/login")
def product(request, id):
    product = product_repo.get_product(id)
    product.photo = os.path.basename(product.photo.path)
    return render(request, 'product.html',
                  {
                      'product': product,
                      'user_id': request.user.id,
                      'total_cart': product_repo.get_total_products(request.user),
                  }
                  )

@login_required(login_url="/login")
def add_product(request, id):
    product_repo.add_to_cart(id,request.user)
    return redirect('cart')



@login_required(login_url="/login")
def remove_product(request, id):
    product_repo.remove_from_cart(id)
    return redirect('cart')

@login_required(login_url="/login")
def cart(request):
    cart_products= product_repo.get_cart(request.user)
    total_prices = sum(cart_product.product_id.price for cart_product in cart_products)
    return render(request, 'cart.html',
                  {
                      'cart_products': cart_products,
                      'user_id': request.user.id,
                      'total_cart' : product_repo.get_total_products(request.user),
                      'total_prices': total_prices,

                  }
                  )


def login_view(request):
    return render(request, 'login.html', {'errorMessage': None})

@login_required(login_url="/login")
def logout_view(request):
    logout(request)
    return redirect('/login')

def submit_login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        user = authenticate(request,
                            username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user is None:
            return render(request, 'login.html'
                          , {'form': form
                              , 'errorMessage': 'Wrong username or password'})
        else:
            login(request, user)
            return redirect('/')
