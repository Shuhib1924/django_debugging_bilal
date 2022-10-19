from django.shortcuts import render
from .models import Blog
# Create your views here.


def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def post(request):
    return render(request, 'post.html')
