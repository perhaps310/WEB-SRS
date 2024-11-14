from django.db import models
from django.utils.translation import gettext_lazy as _

class Project(models.Model):
    title =  models.CharField(max_length=200)
    description =  models.TextField()
    image =  models.ImageField(upload_to='media/projects', blank=True)





# Create your models here.
