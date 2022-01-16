from django.db import models

# Create your models here.
class category(models.Model):
    sweetName=models.CharField(max_length=50, null=False,unique=True)
    class Meta:
        db_table = 'category'
    def __str__(self) :
        return self.sweetName

class product(models.Model):
    souq=models.ForeignKey("souq.Souq",verbose_name="souq", related_name="souq",on_delete=models.CASCADE)
    jumia=models.ForeignKey("jumia.Jumia",verbose_name="jumia", related_name="jumia",on_delete=models.CASCADE)
    noon=models.ForeignKey("noon.Noon",verbose_name="noon", related_name="noon",on_delete=models.CASCADE)


class priceHistory(models.Model):
    souq=models.ForeignKey("souq.Souq",verbose_name="souq", related_name="souqHis",on_delete=models.CASCADE)
    timeDate=models.DateTimeField()
    lastprice = models.CharField(max_length=50, blank=True, null=True)



class notifyme(models.Model):
    username=models.CharField(max_length=200)
    souqid=models.CharField(max_length=200)
    expectedPrice=models.CharField(max_length=200,null=True)
    timeDate=models.DateTimeField(null=True)
    lastPrice=models.CharField(max_length=200)
    # done=models.BooleanField(null=True)
