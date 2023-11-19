from django.shortcuts import render
from .models import Video


def play_list(request):
    param = Video.objects.all()
    return render(request, 'play_list/play_list.html', {'videos': param})


def add_video(request):
    if request.method == 'POST':
        print(request.POST['embed_code'])
        name = request.POST['name']
        embed_code = request.POST['embed_code']
        Video.objects.create(name=name, embed_code=embed_code)

    return render(request, 'play_list/add_video.html')
