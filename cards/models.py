from django.db import models

from accounts import models as accounts_models


class StudySet(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(accounts_models.User, related_name='studysets', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['title', 'user']