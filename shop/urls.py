from django.urls import path
from .views import *


urlpatterns = [
    path('shop/', shop_index, name="shop_index"),
    path('my-shop/', my_products, name="my_products"),
    path('buy/<uuid:id>/', login_required(YandexPayment.as_view()), name="yandex_payments"),
    path('buy/notifications/', YandexNotifications.as_view(), name="yandex_notifications")
]
