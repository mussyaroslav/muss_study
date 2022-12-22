from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from news.forms import NewsForm, UpdateNewsForm
from news.models import News, Category


def news_index(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'news/news_index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {'news': news, 'category': category}
    return render(request, 'news/news_category.html', context)


def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    context = {'news_item': news_item}
    return render(request, 'news/view_news.html', context)


@login_required
def add_news(request):
    if not request.user.is_staff:
        raise PermissionDenied()
    else:
        form = NewsForm()
        if request.method == 'POST':
            form = NewsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('news_index')
        context = {'form': form}
        return render(request, 'news/add_news.html', context)


class UpdateNews(UpdateView):
    model = News
    template_name = 'news/edit_news.html'
    form_class = UpdateNewsForm

    def dispatch(self, request, *args, **kwargs):
        # here you can make your custom validation for any particular user
        if not request.user.is_staff:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)


class DeleteNews(DeleteView):
    model = News
    template_name = 'news/delete_news.html'
    success_url = reverse_lazy('news_index')

    def dispatch(self, request, *args, **kwargs):
        # here you can make your custom validation for any particular user
        if not request.user.is_staff:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)
