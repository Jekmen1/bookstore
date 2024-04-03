from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=150)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    author = models.ForeignKey(Author, related_name='Book', on_delete=models.CASCADE)



