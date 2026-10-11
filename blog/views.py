from django.shortcuts import render
from .models import Post,  Category
from django.views.generic import ListView, DetailView

# Create your views here.

class PostListView(ListView):

    template_name = 'blog/post-list.html'
    # model = Post
    queryset = Post.objects.filter(status=True).select_related('author').prefetch_related('category')
    context_object_name = 'posts'
    paginate_by = 2

class PostDetailView(DetailView):

    template_name = 'blog/post-detail.html'
    queryset = Post.objects.filter(status=True).select_related('author').prefetch_related('category')
    context_object_name = 'post'