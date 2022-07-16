from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def collection(request):
    return render(request, 'pages/collection.html')