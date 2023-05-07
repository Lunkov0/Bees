from django.shortcuts import render


def ad(request):
    return render(request, 'index.html')

def some(request):
    return render(request, 'some.html')


def card(request):
    return render(request, 'card.html')
