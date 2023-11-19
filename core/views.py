from django.shortcuts import render
import random


def reg_form(request):
    return render(request, 'core/reg_form.html')


def magic_number(request):
    if request.method == 'POST':
        if int(request.POST['number']) == random.randint(0, 5):
            return render(request, 'core/magic_number.html', {'result': 'win'})
        else:
            return render(request, 'core/magic_number.html', {'result': 'lose'})
    else:
        return render(request, 'core/magic_number.html')
