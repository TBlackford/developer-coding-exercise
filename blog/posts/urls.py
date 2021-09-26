from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.PostsView.as_view(), name='posts'),
    path('<slug:slug>/', views.PostView.as_view(), name='post'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
