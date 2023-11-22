from django.db import models

class InputSentence(models.Model):
    sentence = models.TextField()