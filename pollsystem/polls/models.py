from django.db import models


# Create your models here.
# Here, I have made two tables one is for questions and the other one is for the choices.
# Each choice is associated with the question

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    p_date = models.DateTimeField('publishing date')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text