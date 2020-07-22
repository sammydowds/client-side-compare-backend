from django.contrib import admin
from django.urls import path 
from repovotes import views 

urlpatterns = [
    path('votes/', views.RepoList.as_view()), 
    path('castvote/', views.SubmitVote.as_view())
]