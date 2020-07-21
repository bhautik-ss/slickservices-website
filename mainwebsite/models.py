from django.db import models

# Create your models here.

class visitorquery(models.Model):
    first_name = models.CharField(max_length=50,default="")
    last_name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=150,default="")
    contactnumber = models.CharField(max_length=20,default="")
    message = models.CharField(max_length=500,default="")
    dateandtime = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.first_name + "" + self.last_name