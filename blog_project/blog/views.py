from django.shortcuts import render
from django.http import Http404,HttpResponse
from .models import blog
# Create your views here.
def home(request):
    return render(request,'blog/index.html')

def blogg(request):
    blog_item = blog.objects.all()
    context = {'a':blog_item}
    return render(request,'blog/blog.html',context)

def det_blog(request,name):
    try:
        fil_blog = blog.objects.get(slug=name)
        context = {'i' : fil_blog}
        return render(request,'blog/blog_det.html',context)
    except:
        raise Http404()

def about(request):
    return render(request,'blog/about_us.html')

def make_blog(request):
    return render(request,'blog/form.html')