#특정뷰함수와 매핑해주는 파일
from django.urls import path
from . import views


app_name = 'questions'
# /articles/ __
urlpatterns = [
    path('', views.index, name='index'),
    path('vote/', views.vote, name='vote'),
    # path('<int:article_pk>/', views.detail, name='detail'),
    # # path('new/', views.new, name='new'),
    # # create로 들어갈거라서 new는 없앰 - 하나로 합칠거임
    # path('create/', views.create, name='create'),
    # # /articles/4/delete/
    # path('<int:article_pk>/delete/',views.delete, name='delete'),
    # path('<int:article_pk>/update/', views.update, name='update'),
    # path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),
    # path('<int:article_pk>/<int:comment_pk>/comments_delete/', views.comments_delete, name='comments_delete'),
    # path('selected/', views.selected, name='selected'),
]
