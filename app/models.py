from django.db import models


class Patient(models.Model):
    user_name = models.CharField(max_length=40, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name


class Survey(models.Model):
    author = models.CharField(max_length=40)
    question1 = models.IntegerField()
    question2 = models.IntegerField()
    question3 = models.IntegerField()
    question4 = models.IntegerField()
    question5 = models.IntegerField()
    question6 = models.IntegerField()
    question7 = models.IntegerField()
    question8 = models.IntegerField()
    question9 = models.IntegerField()
    question10 = models.IntegerField()
    question11 = models.IntegerField()
    question12 = models.IntegerField()
    delay_counter = models.IntegerField(null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "" #self.answers


class SkipSurvey(models.Model):
    user_name = models.CharField(max_length=40, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

