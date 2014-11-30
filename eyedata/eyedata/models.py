from django.db import models

class DataSet(models.Model):
  name = models.CharField(max_length=30)
  location = models.CharField(max_length=180)
  views = models.IntegerField(default=0)
  data = []
