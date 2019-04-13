from rest_framework import generics

from . import models
from . import serializers

class ListCreateStudySet(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = models.StudySet.objects.all()
    serializer_class = serializers.StudySetSerializer

class RetrieveUpdateDestroyStudySet(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = models.StudySet.objects.all()
    serializer_class = serializers.StudySetSerializer