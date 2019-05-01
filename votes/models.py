from django.db import models

class Question(models.Model):
    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choix(models.Model):
    def __str__(self):
        return self.choix_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choix_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)