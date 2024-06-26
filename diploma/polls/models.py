import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('дата публикации')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
class Search(models.Model):
    search_query = models.TextField()
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('дата публикации', default=timezone.now)

    def __str__(self):
        return self.search_query

class Poll(models.Model):
    title = models.CharField(max_length=200)

class Answer(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    option = models.CharField(max_length=200)
