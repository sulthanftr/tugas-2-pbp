from random import choices
from django.db import models

class MyWatchList(models.Model):
    choices = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    watched = models.BooleanField()
    title = models.CharField(max_length=100)
    rating = models.IntegerField(choices=choices, default=1)
    release_date = models.DateField()
    review = models.TextField(max_length=500)
