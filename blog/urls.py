from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.StartPageView.as_view(), name="starting-page"),  # main
    path("posts", views.AllPostsView.as_view(), name="posts-page"),  # /posts
    # allows only slug format i.e. hiphens, no other special cases
    path("posts/<slug:slug>", views.SinglePostView1.as_view(), name="post-detail-page")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
