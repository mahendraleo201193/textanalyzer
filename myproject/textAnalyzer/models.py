from django.db import models

# Create your models here.

class Profile(models.Model):
   name = models.CharField(max_length = 50)
   file = models.FileField(upload_to = 'files')

   class Meta:
      db_table = "profile"
