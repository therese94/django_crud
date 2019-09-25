from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField() # 문자열 빈 값 저장은 null=True 하지 말기
    
    image = models.ImageField(blank=True)
    # blank: 데이터 유효성과 관련되어있다
    # null: DB와 관련되어 있다.
    # '', Null
    created_at = models.DateTimeField(auto_now_add=True)        # 이거중요
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
   # on_delete=models.CASCADE == 'Article이 삭제되면 Comment도 함께 삭제'
   article = models.ForeignKey(Article, on_delete=models.CASCADE)
   content = models.CharField(max_length=200)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   class Meta:
       ordering = ['-pk']
   def __str__(self):
       return self.content