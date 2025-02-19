from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import ArticleForm
from .models import Article


def article_search_view(request):
    query_dict = request.GET # This is a disctionary
    # query = query_dict.get("id")
    article_obj = None

    try:
        query = int(query_dict.get("id"))
    except:
        query = None
        
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        "object": article_obj,
    }
    return render(request, "articles/search.html", context=context)

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form 
    }
    if form.is_valid():
        article_obj = form.save()
        context['form'] = ArticleForm()
        # context['object'] = article_obj
        # context['created'] = True
    return render(request, "articles/create.html", context=context)

def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)