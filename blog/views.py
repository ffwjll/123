from django.shortcuts import render
from .models import Post


def post_list(request):
    param = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': param})
