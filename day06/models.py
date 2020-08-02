from django.db import models

# Create your models here.
class Users(models.Model):
    CHOICES_GENDER = (
        (0,'null'),
        (1,'男'),
        (2,'女'),
    )
    name = models.CharField(max_length=1024,
                            verbose_name='姓名'
                            )
    gender = models.CharField(max_length=255,
                              choices=CHOICES_GENDER,
                              default=0,
                              verbose_name='性别')