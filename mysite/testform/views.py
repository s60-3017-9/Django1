from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def test1(request):
    return render(request,'testform/test1.html')