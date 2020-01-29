from django.db import models

# Model 을 상속받은 Question class
class Question(models.Model):
    question_text = models.CharField(max_length=100) # 좋아하는 색은?
    pub_date = models.DateTimeField('date published')
    class Meta:
        db_table = 'question'
        # atomic = False
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
