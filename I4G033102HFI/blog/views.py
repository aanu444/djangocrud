from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView;
from .models import Post


# Create your views here.
class PostListView(ListView):
    model=Post

class PostCreateView(CreateView):
    model=Post
    fields=[
        "__all__"
    ]
    success_url:reverse_lazy("blog:all")

class postDetailView(DetailView):
    model=Post

class postUpdateView(UpdateView):
    model=Post
    fields=[
        "__all__"
    ]
    success_url:reverse_lazy("blog:all")

class postDeleteView(UpdateView):
    model=Post
    fields=[
        "__all__"
    ]
    success_url:reverse_lazy("blog:all")