from django.db import models

# Baza de date a site-ului
class Document(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='')
    institution_slug = models.CharField(max_length=50, default='')
    institution = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    requirements = models.CharField(max_length=500)
    links = models.CharField(max_length=100, default='', null=True, blank=True)
    extra = models.CharField(max_length=500, default='', null=True, blank=True)

    def __str__(self):
        return self.slug

class Institution(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    documents = models.CharField(max_length=500)
    links = models.CharField(max_length=100, default='', null=True, blank=True)

    def __str__(self):
        return self.slug
