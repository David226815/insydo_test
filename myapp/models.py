from django.http import request

from django.db import models

# Create your models here.
from insydo_test import settings

"""
Database models for insydo_test project
"""
from django.contrib import admin
from django.db import models
from django.core.validators import MaxValueValidator


class Customer(models.Model):
    """
    Table to store Customer Info.
    """
    c_id = models.AutoField(primary_key=True, db_column='c_id')
    c_name = models.CharField(db_column='c_name', max_length=31, default='')
    c_address = models.TextField(db_column='c_address', default='')
    c_city = models.CharField(db_column='c_city', default='', max_length=50)
    c_email = models.BooleanField(db_column='c_email', default=True)

    # validating a contact no. with MaxValueValidator() as per indian standards
    c_contact = models.BigIntegerField(db_column='c_contact', validators=[MaxValueValidator(9999999999)])
    # c = settings.

    def __unicode__(self):
        # if not request.user.is_staff
        return self.c_name

    def edit_customer(self):
        if not request.user.is_staff:
            return True

# admin.site.register(Customer)


        #
    # class MyAdmin(admin.ModelAdmin):
    #     def has_add_permission(self, request):
    #         return False

