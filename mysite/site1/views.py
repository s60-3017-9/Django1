from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def test1(request):
    var_string = 'Hello,Django'
    var2_list = ['web1','web2','web3']
    temp = loader.get_template('index.html')
    context ={
        'var1': var_string,
        'var2': var2_list
    }
    return HttpResponse(temp.render(context,request))