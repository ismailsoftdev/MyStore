from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/detail', views.product_detail, name='product_detail'),
    path('<int:product_id>/buy', views.buy_now, name='buy_now'),
    path('success/<int:order_id>', views.payment_success, name='payment_success'),
    path('cancel/<int:order_id>', views.payment_cancel, name='payment_cancel'),
]
