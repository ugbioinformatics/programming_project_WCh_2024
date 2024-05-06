from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView, 
    CIRconvert_Views,
    Calculate,
)

urlpatterns = [
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("post/suma/", CIRconvert_Views, name="post_suma"),    
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),  # new
    path("post/<int:pk>/calculate/", Calculate, name="post_calculate"),  # new
    path("post/<int:pk>/show/", BlogDeleteView.as_view(), name="post_show"),  # new

    path("", BlogListView.as_view(), name="home"),
]
