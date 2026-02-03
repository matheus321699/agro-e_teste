from django.db import models

class Truck(models.Model):

    class Meta:
        db_table = 'truck'

    id = models.AutoField(primary_key=True)
    license_plate = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    manufacturing_year = models.IntegerField()
    fipe_price = models.FloatField()



