from django.views import generic
from .models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'