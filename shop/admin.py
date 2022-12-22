from django.contrib import admin

from shop.models import ProductsInShop


class ProductsInShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'category', 'group', 'old_price', 'price')
    list_display_links = ('id', 'product_name')


admin.site.register(ProductsInShop, ProductsInShopAdmin)
