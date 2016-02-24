from django.db import models
from django.forms.models import model_to_dict
from django.contrib import admin
from polymorphic.models import PolymorphicModel

class Product(PolymorphicModel):
    price = models.TextField(null=True, blank = True)
    name = models.TextField(null=True, blank = True)
    description = models.TextField(null=True, blank = True)
    add_date = models.DateTimeField(null= True, blank = True, auto_now_add = True)
    image = models.TextField(null=True, blank = True)

    def __str__(self):
        return 'Product (abstract): %s (%s)' % (self.name, self.add_date)

admin.site.register(Product)

RENTAL_STATUS_CHOICES = (
    ('current', 'Rentable'),
    ('damaged', 'Damaged'),
    ('retired','No Longer Rentable')
)

RENTAL_STATUS_CHOICES_MAP = dict(RENTAL_STATUS_CHOICES)


class RentalProduct(Product):
    #purchase_date = models.TextField(null=True, blank = True)
    status = models.TextField(null=True, blank = True, choices = RENTAL_STATUS_CHOICES)
    #rental = models.ForeignKey('Rental', null = True)

    def __str__(self):
        return 'Rental Product: %s (%s) %s' % (self.name, self.add_date, self.status)

admin.site.register(RentalProduct)


class IndividualProduct(Product):
    CreateDate = models.DateTimeField(null = True, blank = True)
    creator = models.ForeignKey('account.User')

    def __str__(self):
        return 'Individual Product: %s (%s)  %s' % (self.name, self.add_date, self.creator.get_full_name())

admin.site.register(IndividualProduct)

class BulkProduct(Product):
    quantity = models.IntegerField(default = 0)

    def __str__(self):
        return 'Individual Product: %s (%s)  %s' % (self.name, self.add_date, self.quantity)

admin.site.register(BulkProduct)

class Category(models.Model):
    name = models.TextField(null=True, blank = True)
    description = models.TextField(null=True, blank = True)

    def __str__(self):
        return 'Category: %s (%s)' % (self.name, self.description)

admin.site.register(Category)
