from django.shortcuts import render
from django.views.generic.base import View
from .models import Post
from django.views.generic import ListView, DetailView  # new
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # новое
from django.urls import reverse_lazy  # импортируем новые методы#new

from django.views.generic.edit import CreateView  # новое изменение


class PostViews(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'statia/statia.html', {'post_list': posts})


class BlogListView(ListView):  # new
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):  # new
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):  # новое изменение
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'content']


class BlogUpdateView(UpdateView):  # Новый изм
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'content']


class BlogDeleteView(DeleteView):  # Нов
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
