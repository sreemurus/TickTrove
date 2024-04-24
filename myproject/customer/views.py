from django.shortcuts import render, redirect

from customer.forms import CustomerForm


# Create your views here.


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_placing_page')
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})


