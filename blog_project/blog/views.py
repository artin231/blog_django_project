from django.shortcuts import render
from . import base
# Create your views here.
def home(request):
    return render(request,'blog/index.html')

def blog(request):
    context = {'a':base.base}
    return render(request,'blog/blog.html',context)