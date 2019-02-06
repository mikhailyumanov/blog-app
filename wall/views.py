from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Post
from .forms import PostForm


def index(request):
    posts_list = Post.objects.order_by("-pub_date")
    current_name = ""
    return render(request, 'wall/index.html', {'posts_list': posts_list,
                                               'current_name': current_name,
                                               'form': PostForm()})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'wall/post.html', {'post': post})


def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        post_author = form['your_name'].value()
        post_text = form['post_text'].value()
        new_post = Post(post_author=post_author, post_text=post_text,
                        pub_date=timezone.now())
        new_post.save()
    return index(request)
