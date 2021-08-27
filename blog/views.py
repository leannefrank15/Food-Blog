from django.http.response import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from datetime import date

from django.urls.base import reverse
from .models import Post
from .forms import CommentForm
from django.views.generic import ListView
from django.views import View

def get_date(post):
    return post['date']

class StartPageView(ListView):
    template_name = "blog/index.html"
    model=Post
    ordering = ["-date"]
    context_object_name="posts"


    def get_queryset(self):
        queryset = super().get_queryset()
        data=queryset[:3]
        return data


class AllPostsView(ListView):
    template_name="blog/all-posts.html"
    model=Post
    ordering=["-date"]
    context_object_name="all_posts"


class SinglePostView1(View):

    def get(self, request,slug):
        post=Post.objects.get(slug=slug)
        context={
            "post": post,
            "post_tags" : post.tags.all(),
            "comment_form" : CommentForm()
        }
        return render(request, "blog/post-detail.html", context)

    def post(self,request,slug):

        post=Post.objects.get(slug=slug)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))


        context={
            "post": post,
            "post_tags" : post.tags.all(),
            "comment-form" : comment_form
        }

        return render(request, "blog/post-detail.html", context)

    
