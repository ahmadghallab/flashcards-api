from rest_framework import generics

from . import models
from . import serializers

class ListCreateStudySet(generics.ListCreateAPIView):
    queryset = models.StudySet.objects.all()
    serializer_class = serializers.StudySetSerializer