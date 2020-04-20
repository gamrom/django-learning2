from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.

def new(request):
    form = PostForm()
    return render(request, 'new.html', {'form': form})

def create(request):
    if request.method == "POST":
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # Post.objects.create(title= title, content= content)
        # Post.save()
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('main_index')

def show(request):
    post_id = request.GET.get('post_id')
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'show.html', context)
