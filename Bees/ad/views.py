from django.shortcuts import render


def ad(request):
    return render(request, 'index.html')
