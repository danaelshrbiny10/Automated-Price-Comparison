from django.db import models

# Create your models here.


class Info(models.Model):
    name=models.CharField(max_length=100)
    logo=models.ImageField(upload_to='info/')
    description=models.TextField(max_length=300)
    fb_link=models.URLField(max_length=200)
    twitter_link=models.URLField(max_length=200)
    instagram_link=models.URLField(max_length=200)
    adress=models.TextField(max_length=200)
    phone_number=models.CharField(max_length=200)
    email=models.EmailField(max_length=60)





    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Infos'
