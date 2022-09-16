from django.contrib import admin
from django.urls import path
from payment.views import CreateCheckoutSessionView, PaymentLandingPageView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('', PaymentLandingPageView.as_view(), name='landing-page')
]
