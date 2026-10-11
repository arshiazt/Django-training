from django.shortcuts import render
from .models import Post,  Category
from django.views.generic import ListView, DetailView, CreateView
from .forms import PostCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin

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

class PostCreateView(LoginRequiredMixin,CreateView):

    template_name = 'blog/post-create.html'
    form_class = PostCreateForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)