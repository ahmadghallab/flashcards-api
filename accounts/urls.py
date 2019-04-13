from django.urls import path

from . import views

app_name = 'accounts'
 
urlpatterns = [
    path('create/',
        views.CreateUser.as_view(),
        name="user_create"),

    path('<int:pk>/',
        views.RetrieveUpdateDestroyUser.as_view(),
        name="user_detail"),

    path('auth/',
        views.CustomAuthToken.as_view(),
        name='token-auth'),
]
