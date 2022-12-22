from django.shortcuts import render, redirect

from reviews.forms import ReviewsForm
from reviews.models import Reviews


def reviews_index(request):
    reviews = Reviews.objects.all()
    form = ReviewsForm()
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('reviews_index')
    context = {'reviews': reviews, 'form': form}
    return render(request, 'reviews/reviews_index.html', context)


def contact_us(request):
    return render(request, 'reviews/contact_us.html')
