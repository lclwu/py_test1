from django.db import models

# Create your models here.
class Test(models.Model):
    id_name = models.AutoField(primary_key=True)
    titel_name = models.CharField(max_length=30)
    aticel = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'test'
