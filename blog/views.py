from django.shortcuts import render, redirect
from .models import Post


def post_list(request):
    param = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': param})


def post_like(request):
    print(request.POST)
    if request.method == 'POST':
        post_id = request.POST['post_id']
        post = Post.objects.get(id=post_id)
        post.likes += 1
        post.save()
        return redirect('post_list')
