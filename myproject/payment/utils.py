# payment/utils.py

from cart.models import CartItem


def calculate_cart_total(user):
    cart_items = CartItem.objects.filter(user=user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return total_price
