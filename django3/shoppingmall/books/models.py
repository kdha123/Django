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
    intro = models.TextField()
    email = models.EmailField()
    photo=models.ImageField(upload_to='photos/%Y', default='photos/noimg.png')
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        try:
            old = Author.objects.get(id=self.id)
            if old.photo != self.photo:
                old.photo.delete(save=False)
        except:
            pass
        super(Author, self).save(*args, **kwargs)
