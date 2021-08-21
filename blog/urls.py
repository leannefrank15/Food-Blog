from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),  # main
    path("posts", views.posts, name="posts-page"),  # /posts
    # allows only slug format i.e. hiphens, no other special cases
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page")
]