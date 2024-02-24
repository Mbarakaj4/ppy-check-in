from django.db import models

# Create your models here.
class Estudiante(models.Model):
   ci = models.IntegerField()
   date_created = models.DateTimeField(auto_now_add=True)
   date_updated = models.DateTimeField(auto_now=True)