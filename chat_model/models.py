from django.db import models


class Query(models.Model):
    """Definition of Query"""
    question = models.TextField()
    response = models.TextField()

class InputSentence(models.Model):
    sentence = models.TextField()