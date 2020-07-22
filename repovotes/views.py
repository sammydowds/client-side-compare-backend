from django.shortcuts import render
from rest_framework import generics
from repovotes.models import Repo, Voter
from repovotes.serializers import RepoSerializer, VoterSerializer

class RepoList(generics.ListAPIView):
    queryset=Repo.objects.all()
    serializer_class=RepoSerializer

class SubmitVote(generics.CreateAPIView):
    queryset=Voter.objects.all()
    serializer_class=VoterSerializer
    # overriding built in create to include method for updating vote count of selected repo 
    def perform_create(self, serializer):
        serializer.save()
        repo_vote = serializer.data['repovoted'] 
        add_vote_repo = Repo.objects.get(id=repo_vote).add_vote()





