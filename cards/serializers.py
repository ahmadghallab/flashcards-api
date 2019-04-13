from rest_framework import serializers

from . import models

class StudySetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'user', 'created_at')
        model = models.StudySet