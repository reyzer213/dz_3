from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    date = models.DateField()
    genre = models.CharField(max_length=100)

class Member(models.Model):
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.EmailField()

class Screening(models.Model):
    film = models.ForeignKey('Movie', on_delete=models.CASCADE)
    date = models.DateField()
    place = models.CharField(max_length=100)
    members = models.ManyToManyField(Member)

    def __str__(self):
        return self.film.name
