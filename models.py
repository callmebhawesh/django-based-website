from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=125)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
     return self.name


# make migrations - create changes and store in a file
# migrate - apply the pending changes made by make migrations