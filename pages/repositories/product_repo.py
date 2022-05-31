from django.contrib.auth.models import User

from ..models import Product, Cart, CartProduct


class ProductRepo:

    def __int__(self):
        pass

    def get_products(self):
        return Product.objects.order_by('-name')

    def get_product(self,id):
        return Product.objects.get(id=id)

    def get_cart(self,user):
        cart = self.check_cart(user)
        return CartProduct.objects.filter(cart_id=cart)

    def get_total_products(self,user):
        cart = self.check_cart(user)
        return CartProduct.objects.filter(cart_id=cart).count()


    def add_to_cart(self,product_id,user):
        cart = self.check_cart(user)
        cart_product = CartProduct()
        cart_product.product_id = Product.objects.get(id=product_id)
        cart_product.cart_id = cart
        cart_product.save()
        return cart.id;

    def check_cart(self,user):
        cart = Cart.objects.get(user_id=user)
        if cart:
            return cart
        cart = Cart()
        import uuid
        cart.id = uuid.uuid4()
        cart.user_id_id = user.id
        cart.save()
        return cart



    def remove_from_cart(self,id):
         return CartProduct.objects.get(id=id).delete()

