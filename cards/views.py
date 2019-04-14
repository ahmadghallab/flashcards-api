from rest_framework import generics

from . import models
from . import serializers

class ListCreateStudySet(generics.ListCreateAPIView):
    queryset = models.StudySet.objects.all()
    serializer_class = serializers.StudySetSerializer

class RetrieveUpdateDestroyStudySet(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StudySet.objects.all()
    serializer_class = serializers.StudySetSerializer

class ListCreateCard(generics.ListCreateAPIView):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer

    def get_queryset(self):
        return self.queryset.filter(
            studyset_id=self.kwargs.get('studyset_id')
        ).order_by('-order')

class RetrieveUpdateDestroyCard(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer