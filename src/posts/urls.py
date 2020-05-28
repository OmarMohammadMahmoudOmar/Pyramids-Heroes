from django.urls import path
from .views import index, blog, about, search, article_detail
urlpatterns = [
    path('', index, name='home'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
    path('search/', search, name='search'),
    path('blog/<id>/', article_detail, name='article'),
]
