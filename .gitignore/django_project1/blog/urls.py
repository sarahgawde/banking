from django.conf.urls import url,include
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    url(r'', PostListView.as_view(), name='blog-home'),
    url(r'^user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    url(r'^post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    url(r'^post/new/', PostCreateView.as_view(), name='post-create'),
    url(r'^post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    url(r'^post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    url(r'^about/', views.about, name='blog-about'),
]
