from django.urls import path
from .views import index, blog, about
urlpatterns = [
    path('', index, name='home'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
]
