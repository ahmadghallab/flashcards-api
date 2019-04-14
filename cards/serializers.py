from rest_framework import serializers

from . import models

class StudySetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'user', 'is_public', 'created_at')
        model = models.StudySet

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'term', 'definition', 'color', 'studyset', 'created_at')
        model = models.Card