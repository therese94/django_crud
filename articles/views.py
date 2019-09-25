from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment

# Create your views here.

# articles 의 메인페이지, articles list 를 보여줌
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

# variable routing으로 사용자가 보기를 원하는 페이지 pk를 받아서
# detail 페이지를 보여준다.
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    comments = article.comment_set.all()

    context = {
        'article':article,
        'comments':comments,
        }
    return render(request, 'articles/detail.html', context)

# 입력페이지 제공
# GET /articles/create/ - 이경우에는 페이지만 받아가는것
# def new(request):
#     embed()
#     return render(request, 'articles/new.html')
    

# 데이터를 전달받아서 article 생성
# POST /articels/create 
def create(request):
    
    # 만약 POST요청으로 사용자 데이터 받아서 article 생성
    # /articles/new/ 의 new.html 의 form 에서 전달받은 데이터들
    if request.method == 'POST':
        title = request.POST.get('title') # 데이터 따오기
        content = request.POST.get('content')
        image = request.FILES.get('image')
        article = Article(title=title, content=content, image=image)
        # article.title = title
        # article.content = content
        article.save()
        # return render(request, 'articles/create.html')
    
        return redirect('articles:detail',article.pk)

    # 만약 GET요청으로 들어오면 html페이지 rendering
    else:
        return render(request, 'articles/create.html')

# 사용자로부터 받은 article_pk값에 해당하는 article을 삭제한다.
def delete(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article_pk)

def update(request, article_pk):
    # POST : 실제 update 로직이 수행
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        if image:
            article.image = image
        article.title = title
        article.content = content
        article.save()
        return redirect('articles:detail', article.pk)
    # GET : update를 하기 위한 Form 을 제공하는 페이지
    else:
        
        context = {'article':article}
        return render(request,'articles/update.html', context)

def comments_create(request, article_pk):
    # article_pk에 해당하는 article에 새로운 comment 생성
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        comment = Comment()
        comment.content = content
        comment.article = article
        comment.save()
    # 생성한 다음 article detail page로 redirect
        return redirect('articles:detail', article.pk)
    

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)

def selected(request):
    chks = request.POST.getlist('chk')
    for chk in chks:
        article = Article.objects.get(pk=chk)
        article.delete()
    return redirect('articles:index')


