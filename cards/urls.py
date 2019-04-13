from django.urls import path

from . import views

app_name = 'apiv1'

urlpatterns = [
    path('studysets/',
        views.ListCreateStudySet.as_view(),
        name='studysets_list'
    ),
    path('studysets/<int:pk>/',
        views.RetrieveUpdateDestroyStudySet.as_view(),
        name='studysets_detail'
    ),
]