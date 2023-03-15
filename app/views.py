from django.shortcuts import render

# Create your views here.
def simple_if(request):
    d={'a':'30','b':'20'}
    return render(request,'simple_if.html',d)

def simple_if_else(request):
    d={'a':'10','b':'30'}
    return render(request,'simple_if_else.html',d)

def simple_if_elif_else(request):
    d={'a':'31','b':'40','c':'50'}
    return render(request,'simple_if_elif_else.html',d)

def nested_if(request):
    d={'a':'31','b':'40','c':'50'}
    return render(request,'nested_if.html',d)

def for_loop(request):
    d={'name':'jyothi'}
    return render(request,'for_loop.html',d)
