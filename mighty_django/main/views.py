from django.shortcuts import render
from . import urls
from posts.models import Post
# Create your views here.

def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'main/index.html', context)
