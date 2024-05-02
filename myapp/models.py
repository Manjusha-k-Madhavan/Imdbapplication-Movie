from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=200,unique=True)
    language=models.CharField(max_length=200)
    run_time=models.PositiveBigIntegerField()
    genre=models.CharField(max_length=200)
    director=models.CharField(max_length=200)
    year=models.PositiveBigIntegerField()
    actors=models.CharField(max_length=200)


    def __str__(self):
        return self.name