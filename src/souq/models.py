from django.db import models


class Souq(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True)
    manufacture = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField()
    img = models.TextField()
    url = models.TextField(default="")
    ean = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    lastprice = models.CharField(max_length=50, blank=True, null=True)
    souqId = models.TextField()
    rate = models.FloatField()
    category=models.ForeignKey("products.category",verbose_name="category", related_name="souq",on_delete=models.CASCADE,default=1)

    class Meta:
        db_table = 'souq'