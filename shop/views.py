import uuid

from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.views import View
from yookassa import Payment
from .models import ProductsInShop
from yookassa import Configuration
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


def shop_index(request):
    products = ProductsInShop.objects.all()
    context = {'products': products}
    return render(request, 'shop/shop_index.html', context)


@login_required
def my_products(request):
    return render(request, 'shop/my_products.html')
# def process_shop(self, request):
#     payment_form = PaymentForm()
#     if payment_form.is_valid():
#         # Добавить пользователя в соответствующую группу
#         try:
#             group = self.ProductsInShop.group
#             group.user_set.add(request.user)
#         except AttributeError:
#             # Нет группы, в которую можно было бы добавить пользователя
#             pass
#     return True


class YandexPayment(View):
    def get(self, request, id):
        item = ProductsInShop.objects.get(id=id)
        Configuration.account_id = '54401'
        Configuration.secret_key = 'test_Fh8hUAVVBGUGbjmlzba6TB0iyUbos_lueTHE-axOwM0'
        idempotence_key = str(uuid.uuid4())
        payment = Payment.create({
            "amount": {
                "value": item.price,
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "http://127.0.0.1:8000/"
            },
            "capture": True
        }, idempotence_key)
        return redirect(payment.confirmation.confirmation_url)


class YandexNotifications(APIView):
    def post(self, request):
        item = ProductsInShop.objects.get(id=id)
        payment_id = '215d8da0-000f-50be-b000-0003308c89be'
        Payment.capture(payment_id)
        basic = Group.objects.get(name=item.group)
        basic.user_set.add(request.user)
        return redirect('home')
