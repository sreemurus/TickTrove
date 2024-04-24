# payment/views.py

from django.shortcuts import render, redirect
from .forms import PaymentForm
from cart.models import CartItem
from .utils import calculate_cart_total

from .models import Order, OrderItem


def initiate_payment(request):
    total_price = calculate_cart_total(request.user)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            # Create an order and associate it with the user and items in the cart
            order = Order.objects.create(user=request.user, total_amount=total_price)
            # Retrieve items from the cart and create order items
            cart_items = CartItem.objects.filter(user=request.user)
            for cart_item in cart_items:
                OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity)
            return render(request, 'payment_page.html', {'amount': amount, 'total_price': total_price})
    else:
        form = PaymentForm(initial={'amount': total_price})

    return render(request, 'payment_form.html', {'form': form, 'total_price': total_price})


def payment_success(request):
    payment_id = request.GET.get('razorpay_payment_id')

    # Retrieve the cart associated with the user
    cart = CartItem.objects.filter(user=request.user).first()

    if cart:
        # Remove the cart
        cart.delete()

    return render(request, 'payment_success.html', {'payment_id': payment_id})


def payment_failure(request):
    payment_id = request.GET.get('razorpay_payment_id')
    return render(request, 'payment_failure.html', {'payment_id': payment_id})
