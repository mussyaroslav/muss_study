from django.urls import path
from .views import *


urlpatterns = [
    path('news/', news_index, name="news_index"),
    path('news/category/<int:category_id>/', get_category, name="news_category"),
    path('news/<int:news_id>/', view_news, name="view_news"),
    path('news/add_news/', add_news, name="add_news"),
    path('news/edit/<int:pk>/', login_required(UpdateNews.as_view()), name="edit_news"),
    path('news/remove/<int:pk>/', login_required(DeleteNews.as_view()), name="delete_news")
]
