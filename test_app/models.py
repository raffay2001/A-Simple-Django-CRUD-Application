from django.db import models

# Create your models here.
class Person(models.Model):
    f_name = models.CharField(max_length=255, null=False, blank=False)
    l_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)


    def __str__(self):
        return f"{self.f_name} {self.l_name}"

    
