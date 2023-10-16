from django.shortcuts import redirect, render
from .models import Post, Category1, Category2
from django.contrib import messages

# Create your views here.

def HomePage(request):
    get_all_posts = Post.objects.all()
    get_all_categories_in_category_1 = Category1.objects.all()[:2]
    get_all_categories_in_category_2 = Category2.objects.all()[:2]
    context  = {
        'posts':get_all_posts,
        'cat1': get_all_categories_in_category_1,
        'cat2': get_all_categories_in_category_2
    }
    return render(request, 'blogapp/index.html', context)