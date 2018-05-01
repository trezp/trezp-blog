from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . models import Post, Log
# Create your views here.

class LogListView(ListView): 
  model = Log
  template_name = 'home.html'

class LogDetailView(DetailView):
  model = Log
  template_name = 'log_detail.html'

class BlogListView(ListView):
  model = Post
  template_name = 'home.html'

class BlogDetailView(DetailView):
  model = Post
  template_name = 'post_detail.html'

class BlogCreateView(CreateView):
  model = Post
  template_name = 'post_new.html'
  fields = '__all__'

class BlogUpdateView(UpdateView):
  model = Post
  fields = ['title', 'body']
  template_name = 'post_edit.html'

class BlogDeleteView(DeleteView):
  model = Post
  template_name = 'post_delete.html'
  success_url = reverse_lazy('home')
