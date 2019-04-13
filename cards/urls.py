from django.urls import path

from . import views

app_name = 'apiv1'

urlpatterns = [
    path('studysets/',
        views.ListCreateStudySet.as_view(),
        name='sets_list'
    ),
]