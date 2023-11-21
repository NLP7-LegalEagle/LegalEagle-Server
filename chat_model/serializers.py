from rest_framework import serializers

from .models import InputSentence


class InputSentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputSentence
        fields = ('sentence',)