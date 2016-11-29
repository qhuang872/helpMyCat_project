# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class LostFoundAdoptablePets(models.Model):
    data_source = models.TextField(db_column='Data_Source', blank=True, null=True)  # Field name made lowercase.
    record_type = models.TextField(db_column='Record_Type', blank=True, null=True)  # Field name made lowercase.
    link = models.TextField(db_column='Link', blank=True, null=True)  # Field name made lowercase.
    current_location = models.TextField(db_column='Current_Location', blank=True, null=True)  # Field name made lowercase.
    animal_name = models.TextField(db_column='Animal_Name', blank=True, null=True)  # Field name made lowercase.
    animal_type = models.TextField(blank=True, null=True)
    age = models.TextField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    animal_gender = models.TextField(db_column='Animal_Gender', blank=True, null=True)  # Field name made lowercase.
    animal_breed = models.TextField(db_column='Animal_Breed', blank=True, null=True)  # Field name made lowercase.
    animal_color = models.TextField(db_column='Animal_Color', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    date_type = models.TextField(db_column='Date_Type', blank=True, null=True)  # Field name made lowercase.
    obfuscated_address = models.TextField(db_column='Obfuscated_Address', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    zip = models.IntegerField(db_column='Zip', blank=True, null=True)  # Field name made lowercase.
    jurisdiction = models.TextField(blank=True, null=True)
    obfuscated_latitude = models.FloatField(blank=True, null=True)
    obfuscated_longitude = models.FloatField(blank=True, null=True)
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    image_alt_text = models.TextField(blank=True, null=True)
    location_for_map = models.TextField(blank=True, null=True)
    memo = models.TextField(db_column='Memo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lost__found__adoptable_pets'
