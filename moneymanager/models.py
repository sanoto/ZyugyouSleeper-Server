from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField("名前", max_length=20)
    user_id = models.IntegerField("学籍番号", primary_key=True)
    felica_id = models.CharField("FelicaID", max_length=100)
