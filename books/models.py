from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=64)
    year = models.PositiveSmallIntegerField()
    description = models.TextField()
    category = models.ForeignKey(
        to='Category',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=64)

