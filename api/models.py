from django.db import models

# Create your models here.
class OtherField(models.Model):
    id = models.AutoField(primary_key=True)
    other = models.TextField(blank=True)

class Main(models.Model):
    sender = models.IntegerField()
    datetime = models.DateTimeField()
    priority = models.IntegerField()
    description = models.TextField()
    other_fk = models.ForeignKey(OtherField,on_delete=models.CASCADE)