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
        'stripe_public_key_':'pk_test_51IDByNHqlGOLXRqaHYzfR2Kt02UX9EDBJDup5fPAPkMRIrx8IfaBbPo7r2oIgKOK2iZGQ163oOdvEGL7djBF2V3r00Nu5sALwi',
        'client_secret': 'test client secret', 
    }

    return render(request, template, context)