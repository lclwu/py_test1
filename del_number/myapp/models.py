# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class PpdName(models.Model):
    customer_name = models.CharField(max_length=90, blank=True, null=True)
    identity_no = models.CharField(max_length=19, blank=True, null=True)
    mobile_phone = models.CharField(max_length=15, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ppd_name'

# class City(models.Model):
#     id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=35)  # Field name made lowercase.
#     countrycode = models.ForeignKey('Country', models.DO_NOTHING, db_column='CountryCode')  # Field name made lowercase.
#     district = models.CharField(db_column='District', max_length=20)  # Field name made lowercase.
#     population = models.IntegerField(db_column='Population')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'city'
#

