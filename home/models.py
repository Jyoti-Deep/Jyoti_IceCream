from django.db import models

# Create your models here.
class Contact(models.Model):
    input1 = models.CharField(max_length=122)
    input2 = models.CharField(max_length=122)
    input3 = models.CharField(max_length=122)
    input4 = models.CharField(max_length=122)
    input5 = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self) :
        return self.input1 + self.input2

   