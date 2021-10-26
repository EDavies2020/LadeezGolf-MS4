from django.shortcuts import render


from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JokR8Ha3rMGgsAfWligA5A0TAtcGjbhvTX7Ij1JBBlWu0x7EaW2hxM6KsKOPVH3olNgs2hl60blfDzh6AAdGHf400a4bk5pf6'
    }

    return render(request, template, context)
