from django.db import models
from django.contrib.auth.models import AbstractUser
# Define models here

class User(AbstractUser):
    Address1 = models.TextField(null= True, blank = True)
    Address2 = models.TextField(null= True, blank = True)
    ZipCode = models.TextField(null= True, blank = True)
    City = models.TextField(null= True, blank = True)
    State = models.TextField(null= True, blank = True)
    Phone = models.TextField(null= True, blank = True)
    BirthDate = models.DateField(null = True, blank = True)

    def __str__(self):
        return 'User: %s (%s)' % (self.get_full_name(), self.username)
