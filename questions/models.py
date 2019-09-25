from django.db import models

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=20)

class Choice(models.Model):
    # on_delete=models.CASCADE == 'Article이 삭제되면 Comment도 함께 삭제'
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    content = models.CharField(max_length=20)
    votes = models.IntegerField()