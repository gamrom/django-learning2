from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.views.decorators.http import require_POST
# Create your views here.

def new(request):
    form = PostForm()
    return render(request, 'posts/new.html', {'form': form})

@require_POST
def create(request):
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # Post.objects.create(title= title, content= content)
    # Post.save()
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
    # return redirect('main_index')
    return redirect(form.instance)

def show(request, post_id):
    # post_id = request.GET.get('post_id')
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/show.html', context)

def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post,
        'form': PostForm(instance=post)
    }
    return render(request, 'posts/edit.html', context)

def update(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST, instance = post)
    if form.is_valid():
        form.save()
    return redirect(post)

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('main_index')
