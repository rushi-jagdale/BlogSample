from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from core.models import Blog
from django.views.generic.edit import UpdateView 
from core.forms import BlogForm

# Create your views here.

def listing(request):
    data = {
        "blogs": Blog.objects.all()
    }

    return render(request, "listing.html", data)

def view_blog(request, blog_id):
    # blog = get_object_or_404(Blog, id=blog_id)
    blog = Blog.objects.get(id = blog_id)
    data = {
        "blog":blog,
    }

    return render(request, "view_blog.html", data)

def update(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    form = BlogForm(request.POST, instance=blog)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "view_blog.html", data)

def destroy(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    blog.delete()
    return redirect("/")   