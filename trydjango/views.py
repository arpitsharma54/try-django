"""
To render html web pages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string

from articles.models import Article


def home_view(request, id=None, *args, **kwargs):
    """
    Take in a request (Django sneds request)
    Return HTML as a response (We pick to return the response)
    """
    name = "Arpit"
    number = random.randint(1, 23)

    article_obj = Article.objects.get(id=number)
    article_queryset = Article.objects.all()

    context = {
        "object_list": article_queryset,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
    }

    
    HTML_STRING = render_to_string("home-view.html", context=context)

    return HttpResponse(HTML_STRING)