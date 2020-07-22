from django.db import models

class Repo(models.Model):
    link = models.TextField(); 
    name = models.TextField(); 
    votes = models.IntegerField(); 

    def add_vote(self):
        self.votes += 1
        self.save()


class Voter(models.Model):
    email = models.TextField(unique=True); 
    repovoted = models.IntegerField(); 