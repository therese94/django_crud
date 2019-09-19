#특정뷰함수와 매핑해주는 파일
from django.urls import path
from . import views

# /articles/ __
urlpatterns = [
    path('', views.index),
    path('<int:article_pk>/', views.detail),
    path('new/', views.new),
    path('create/', views.create),
    # /articles/4/delete/
    path('<int:article_pk>/delete/',views.delete),
    
]
