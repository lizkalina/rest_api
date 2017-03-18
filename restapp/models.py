from __future__ import unicode_literals

class Person(models.Model):
    name = models.CharField(max_length=100)
    favorite_city = models.CharField(max_length=100)
