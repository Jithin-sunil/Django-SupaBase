from django.db import models

# Create your models here.
# models.py

from django.db import models

class District(models.Model):
    district_name = models.CharField(max_length=255)


