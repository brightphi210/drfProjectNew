from django.db import models

# Create your models here.
class Todoapp(models.Model):
   titles = models.CharField(max_length=250, blank=True, null=True )
   description = models.TextField(max_length=500, blank=True, null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   completed = models.BooleanField(default=False)

   def __str__(self):
      return self.titles

      
