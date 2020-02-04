from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    Publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    authors = models.ManyToManyField('Author')
    pub_date = models.DateField()
    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    website = models.URLField()
    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)
    intro = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.name