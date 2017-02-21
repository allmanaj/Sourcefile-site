from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse

from .models import Comment, Post


# Create your views here.
def detail(request, post_id):
    post=get_object_or_404(Post, pk=post_id)
    recent_comments = Comment.objects.filter(post=post_id)
    return render(request, 'blog/detail.html', {'post':post, 'recent_comments': recent_comments})

def feed(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/feed.html', context)

def post_comment(request, post_id):
    comment_poster = request.POST['comment_poster']
    comment_text = request.POST['comment_body']

    c = Comment(comment_poster_name=comment_poster, comment_body=comment_text, pub_date=timezone.now())
    c.post_id = post_id
    c.save()

    return HttpResponseRedirect(reverse('blog:detail', args=(post_id, )))
