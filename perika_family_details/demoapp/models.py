from django.db import models

# Create your models here.

class FamilyDetails(models.Model):

    hno = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=100)
    ownername = models.CharField(max_length=100)
    uscno = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    mothername = models.CharField(max_length=100)

    child1name = models.CharField(max_length=100)
    child1age = models.CharField(max_length=100)
    child1education = models.CharField(max_length=100)

    child2name = models.CharField(max_length=100)
    child2age = models.CharField(max_length=100)
    child2education = models.CharField(max_length=100)

    child3name = models.CharField(max_length=100)
    child3age = models.CharField(max_length=100)
    child3education = models.CharField(max_length=100)

    village = models.CharField(max_length=100)
    Mandal = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    State =  models.CharField(max_length=100)

