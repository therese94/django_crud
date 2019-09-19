from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

# articles 의 메인페이지, articles list 를 보여줌
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

# variable routing으로 사용자가 보기를 원하는 페이지 pk를 받아서
# detail 페이지를 보여준다.
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article':article}
    return render(request, 'articles/detail.html', context)

# 입력페이지 제공
def new(request):
    return render(request, 'articles/new.html')
    

# 데이터를 전달받아서 article 생성
def create(request):
    # /articles/new/ 의 new.html 의 form 에서 전달받은 데이터들
    title = request.GET.get('title') # 데이터 따오기
    content = request.GET.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()
    # <a href
    # return render(request, 'articles/create.html')
    
    return redirect('articles:detail',article.pk)

# 사용자로부터 받은 article_pk값에 해당하는 article을 삭제한다.
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')
