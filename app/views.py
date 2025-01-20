from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
import stripe
from  .models import Product, Order


# Set the stripe api key
stripe.api_key = settings.STRIPE_SECRET_API_KEY


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_detail.html', {'product': product})


def buy_now(request, product_id):
    try:
        product = get_object_or_404(Product, pk=product_id)
        
        order = Order.objects.create(
            product=product,
            quantity=1,
        )
        
        # Create a Stripe checkout session, passing in the product data
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',  # Specify the currency here
                        'product_data': { 
                            'name': product.name,
                            'description': product.description,
                        },
                        'unit_amount': int(product.price * 100), # Convert the original price to cents
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('payment_success', args=[order.pk])),
            cancel_url=request.build_absolute_uri(reverse('payment_cancel', args=[order.pk])),
            metadata={
                'order_id': order.pk,
                'product_id': product.pk,
            },
        )
        
        # Redirect the user to the Stripe checkout page
        return redirect(checkout_session.url, code=303)

    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found.'}, status=404)


def payment_success(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    
    # Update the order status to "paid"
    order.paid = True
    order.paid_at = timezone.now()
    order.save()
    return render(request, 'payment_success.html', {'order': order})


def payment_cancel(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'payment_cancel.html', {'order': order})
