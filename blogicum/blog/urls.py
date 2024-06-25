from django.urls import path, include

from . import views
from django.conf import settings

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
    path('posts/<slug:pk>/', views.post_detail, name='post_detail'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
