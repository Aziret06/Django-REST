from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=350)
    description = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=8, blank=True, null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')
    # rating =

    def movies_reviews(self):
        return self.reviews

    def __str__(self):
        return self.title


STARS = (
    (i, i * '⭐️') for i in range(1, 6)
)


class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(choices=STARS, default=5)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')


    def __str__(self):
        return self.text
