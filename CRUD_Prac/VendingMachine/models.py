from django.db import models


class BeverageList(models.Model):
    title = models.CharField(max_length=150)
    photo = models.FileField(null=True, blank=True)
    price = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return self.title
