from django.db import models

from accounts import models as accounts_models


class StudySet(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(accounts_models.User, related_name='studysets', on_delete=models.CASCADE)
    is_public = models.BooleanField(null=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['title', 'user']

class Card(models.Model):
    term = models.CharField(max_length=50)
    definition = models.CharField(max_length=250)
    color = models.CharField(max_length=15)
    studyset = models.ForeignKey(StudySet, related_name='cards', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
