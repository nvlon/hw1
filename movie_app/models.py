from django.db import models

class Director(models.Model):
    id = models.UUIDField(primary_key=True, default=True)
    name = models.CharField(max_length=100)



    def __str__(self):
        return self.name


class Movie(models.Model):
    class Meta:
        verbose_name_plural='Movie'
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(default=0)
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    duration = models.DurationField(default=True)
    director = models.ForeignKey(Director,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField(blank=True, null=True)
    movie = models.ForeignKey(Movie,on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return self.text
