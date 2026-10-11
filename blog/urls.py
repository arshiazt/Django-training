from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('post/',views.PostListView.as_view(),name='post-list'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post-detail'),
    path('post/create/',views.PostCreateView.as_view(),name='post-create'),
]