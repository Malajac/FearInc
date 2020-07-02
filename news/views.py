from django.shortcuts import render
from django.http import HttpResponse
from .models import News

import json

def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': 'News list'
    }
    return render(request, 'news/index.html', context)


def test(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')
