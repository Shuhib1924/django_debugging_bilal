from django.shortcuts import render
from .models import Blog
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    blogs = Blog.objects.all().order_by('-post_created')
    context = {
        'blogs': blogs,
    }
    return render(request, 'home.html', context)


class Detail(DetailView):
    model = Blog
    template_name = 'detail.html'
    context_object_name = 'blog'


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


class Post(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'post.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
