from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse ('<h1>Hello homepage</h1>')
    index = 'index'
    context = {'homepage': index}
    return render(request, 'homepage/home.html', context)
