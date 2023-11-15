from rest_framework import serializers

from .models import InputSentence, Query


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ('question', 'response')

class InputSentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputSentence
        fields = ('sentence',)