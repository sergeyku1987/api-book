from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=64)
    year = models.PositiveSmallIntegerField()
    description = models.TextField()
    category = models.ForeignKey(
        to='Category',
        on_delete=models.PROTECT
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    updeate_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=64)

