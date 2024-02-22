from django.urls import path
from .views import renderPosts, post_detail

app_name = 'blog'

urlpatterns = [
    path('', renderPosts, name="posts"),
    path('<int:post_id>', post_detail, name='post_detail')
]