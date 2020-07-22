
Table of Contents
======================

* [What is this for?](#what-is-this-for?)
* [End Points](#end-points)
* [Models](#models)
* [File Structure](#file-structure)

## What is this for? 
This is a REST API to capture voters and votes for a particular client-side framework. 

## End Points 

Endpoint | HTTP Method | CRUD Method | Result
-- | -- | -- | -- 
`votes` | GET | READ	| Gives JSON of frameworks and their votes 
`castvote`	|POST| CREATE|	Create a voter and incriment vote for framework

## Models 

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

## Built With

* Django 
* Django REST Framework 

## Authors

* **Sammy Dowds** - *Initial work* - [Profile](https://github.com/sammydowds)

## Acknowledgments