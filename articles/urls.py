#특정뷰함수와 매핑해주는 파일
from django.urls import path
from . import views


app_name = 'articles'
# /articles/ __
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # /articles/4/delete/
    path('<int:article_pk>/delete/',views.delete, name='delete'),
    
]
