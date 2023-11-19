from django.shortcuts import render
from .models import Video


def play_list(request):
    param = Video.objects.all()
    return render(request, 'play_list/play_list.html', {'videos': param})
