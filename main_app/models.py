from django.db import models

# Create your models here.


class Widget(models.Model):
    description = models.CharField(max_length=100)
    quanitity = models.IntegerField()

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('index')
