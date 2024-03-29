from rest_framework import generics

from . import models
from . import serializers

class ListCreateStudySet(generics.ListCreateAPIView):
    queryset = models.StudySet.objects.all()
    serializer_class = serializers.StudySetSerializer

    def get_queryset(self):
        return self.queryset.filter(
            user_id=self.kwargs.get('user_id')
        ).order_by('-id')

class RetrieveUpdateDestroyStudySet(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StudySet.objects.all()
    serializer_class = serializers.StudySetSerializer

class ListCreateCard(generics.ListCreateAPIView):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer
    pagination_class = None

    def get_queryset(self):
        return self.queryset.filter(
            studyset_id=self.kwargs.get('studyset_id')
        )

class RetrieveUpdateDestroyCard(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer