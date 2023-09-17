from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.title} - {self.director.name}"
