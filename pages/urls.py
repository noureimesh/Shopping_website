from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('product/<uuid:id>', views.product, name='product'),
    path('add_product/<uuid:id>', views.add_product, name='add_product'),
    path('remove_product/<uuid:id>', views.remove_product, name='remove_product'),
    path('cart', views.cart, name='cart'),
    path('submit_login', views.submit_login, name='submit_login'),
]