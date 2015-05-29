from django.db import models


class Patient(models.Model):
    user_name = models.CharField(max_length=40, primary_key=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_name


class Survey(models.Model):
    author = models.CharField(max_length=40)
    answers = models.CharField(max_length=250)
    choices = models.CharField(max_length=250)
    delay_counter = models.IntegerField(null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answers

