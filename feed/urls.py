from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='all-blogs'),
    re_path(r'^blog/(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='blog-detail'),
    path('authors/', views.AuthorListView.as_view(), name='all-authors'),
    re_path(r'^user/(?P<pk>\d+)$', views.UserDetailView.as_view(), name='user-detail'),
]
