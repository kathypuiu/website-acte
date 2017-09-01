from django.db import models
from jsonfield import JSONField

# Baza de date a site-ului
class Document(models.Model):
    url_name = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='')
    institution = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    requirements = models.CharField(max_length=500)

    def __str__(self):
        return self.url_name

class Institution(models.Model):
    url_name = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    documents = models.CharField(max_length=500)

    def __str__(self):
        return self.url_name
