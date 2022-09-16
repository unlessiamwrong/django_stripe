from django.shortcuts import redirect
from django.views import View
import stripe
from django.conf import settings
from django.views.generic import TemplateView
from .models import Item
stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentLandingPageView(TemplateView):
    template_name = 'landing.html'

    def get_context_data(self, **kwargs):
        item = Item.objects.get(name='Coca-Cola')
        context = super(PaymentLandingPageView, self).get_context_data(**kwargs)
        context.update({
            'item': item,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
        })
        return context


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        domain = 'http://127.0.0.1:8000/'
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1LiJbOF2n4MnDum27cbyiRLf',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return redirect(checkout_session.url, code=303)
