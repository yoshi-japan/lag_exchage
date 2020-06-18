from django.db import models

# Create your models here.


class PostManager(models.Manager):
    pass

class CountryManager(models.Manager):
    pass


class Country(models.Model):
    born = models.CharField(
        'country',
        max_length=216,
    )

    def __str__(self):
        return self.born

    objects = CountryManager()

class Post(models.Model):
    user_name = models.CharField(
        'user_name',
        max_length=32,
    )
    zoom_url = models.CharField(
        "remotehour_url",
        max_length=512,
        blank=False,
        null=False,
    )
    country = models.ForeignKey(
        Country,
        verbose_name = "From",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,

    )
    objects = PostManager()

    def __str__(self):
        return self.user_name

