from django.urls import path
from .views import *


urlpatterns = [
    path('reviews/', reviews_index, name='reviews_index'),
    path('contact-us/', contact_us, name='contact_us')
]
