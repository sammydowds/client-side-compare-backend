from rest_framework import serializers
from repovotes.models import Repo, Voter  

class RepoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Repo 
        fields = ['id', 'name', 'link', 'votes']


class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter 
        fields = ['email', 'repovoted']


