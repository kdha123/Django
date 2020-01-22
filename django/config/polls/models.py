from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=100) # 좋아하는 색은?
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

