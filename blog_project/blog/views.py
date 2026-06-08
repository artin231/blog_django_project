from django.shortcuts import render
from . import base
from django.http import Http404,HttpResponse
# Create your views here.
def home(request):
    return render(request,'blog/index.html')

def blog(request):
    context = {'a':base.base}
    return render(request,'blog/blog.html',context)

def det_blog(request,name):
    context = {'i' : 0}
    for i in base.base:
        print(type(name),type(i['id']))
        if name == i['id']:
            context['i'] = i
    
    if context['i'] != 0:
        return render(request,'blog/blog_det.html',context)
    raise Http404()

def about(request):
    return render(request,'blog/about_us.html')

def make_blog(request):
    return render(request,'blog/form.html')