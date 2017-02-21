from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.
def detail(request, post_id):
    return HttpResponse("This is the page where you can view the post! this post is #%s" % post_id)

def feed(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/feed.html', context)

