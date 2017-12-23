from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import Http404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def home(request):
    return render(request, 'src/home.html')

def detail(request, Post_id):
    try:
        post= Post.objects.get(pk=Post_id)
    except Post.DoesNotExist:
        raise Http404("Post Does Not Exist")
    return render(request,'post/post.html',{'post':post})

def index(request):
    contact_list = Post.objects.all()
    paginator = Paginator(contact_list, 3)

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'post/blog.html', {'contacts': contacts})
