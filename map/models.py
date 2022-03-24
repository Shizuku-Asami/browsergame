from django.db import models

class Terrain(models.Model):
    x = models.SmallIntegerField()
    y = models.SmallIntegerField()
    image = models.ImageField()

    UNIQUE_TOGETHER = ['x', 'y']

    def __str__(self):
        return f"({self.x}|{self.y})"