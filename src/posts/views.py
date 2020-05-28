from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, reverse
from .models import Article, Subscribe
from django.db.models.query_utils import Q


def index(request):
    feautred_articles = Article.objects.filter(
        is_feautred=True).order_by('-timestamp')[:5]
    latest_articles = Article.objects.order_by('-timestamp')[:3]
    trending_articles = Article.objects.order_by('-view_count')[:3]

    if request.method == 'POST':
        newSubscibe = Subscribe()
        newSubscibe.name = request.POST['name']
        newSubscibe.email = request.POST['email']
        newSubscibe.save()

        return redirect(reverse('home'))

    context = {
        'feautred_articles_5': feautred_articles,
        'latest_articles_3': latest_articles,
    }
    return render(request, 'index.html', context)


def blog(request):
    queryset = Article.objects.all()
    paginator = Paginator(queryset, 9)
    page_request_name = "page"
    page = request.GET.get(page_request_name)
    try:
        paginted_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginted_queryset = paginator.page(1)
    except EmptyPage:
        paginted_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginted_queryset,
        'page_request_name': page_request_name
    }
    return render(request, 'blog.html', context)


def error_404(request, exception):
    return render(request, '404.html')


def about(request):
    return render(request, 'about.html')


def search(request):
    article_list = Article.objects.all()
    query = request.GET.get('q')

    if query:
        article_list = article_list.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query) |
            Q(content__icontains=query)
        ).distinct()

    context = {
        'query': query.title() or 'All The Articles',
        'queryset': article_list
    }
    return render(request, 'search_result.html', context)


def article_detail(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article': article
    }

    return render(request, 'article_detail.html', context)

def contact(request):
    return render(request, 'contact.html', {})