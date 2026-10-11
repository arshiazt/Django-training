from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('post/',views.PostListView.as_view(),name='post-list'),
]