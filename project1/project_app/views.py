from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.http import HttpResponse
from .models import Article  # Подставьте свою модель, если у вас есть

def article_list(request):
    # Получите список всех статей
    articles = Article.objects.all()  # Подставьте свой запрос, чтобы получить список статей
    return render(request, 'myapp/article_list.html', {'articles': articles})

def article_detail(request, article_id):
    # Получите статью по её идентификатору (или другому уникальному полю)
    article = Article.objects.get(id=article_id)  # Подставьте свой запрос, чтобы получить статью
    return render(request, 'myapp/article_detail.html', {'article': article})

