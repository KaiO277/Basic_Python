from django.db import models

# Create your models here.

class Profile(models.Model):
    # user = pass
    # id_user = pass
    profileimg = models.ImageField()


