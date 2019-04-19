from django.urls import path

from . import views

app_name = 'apiv1'

urlpatterns = [
    path('users/<int:user_id>/studysets/',
        views.ListCreateStudySet.as_view(),
        name='studyset_list'
    ),
    path('studysets/<int:pk>/',
        views.RetrieveUpdateDestroyStudySet.as_view(),
        name='studyset_detail'
    ),
    path('studysets/<int:studyset_id>/cards/',
        views.ListCreateCard.as_view(),
        name='card_list'
    ),
    path('cards/<int:pk>/',
        views.RetrieveUpdateDestroyCard.as_view(),
        name='card_detail'
    ),
]