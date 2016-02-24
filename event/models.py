from django.db import models
from django.contrib import admin



# RENTAL_STATUS_CHOICES = {
#     ('current', 'Rentable'),
#     ('damaged', 'Damaged'),
#     ('retired','No Longer Rentable'),
# }
#
# RENTAL_STATUS_CHOICES_MAP = dict(RENTAL_STATUS_CHOICES)


class Venue(models.Model):
    name = models.TextField(null=True, blank = True)
    address = models.TextField(null=True, blank = True)
    city = models.TextField(null=True, blank = True)
    state = models.TextField(null=True, blank = True)
    zip_code = models.TextField(null=True, blank = True)

    def __str__(self):
        return '%s (%s)' % (self.name, self.state)

admin.site.register(Venue)


class Event(models.Model):
    name = models.TextField(null=True, blank = True)
    description = models.TextField(null=True, blank = True)
    start_date = models.DateField(null=True, blank = True)
    end_date = models.DateField(null=True, blank = True)
    venue = models.ForeignKey('Venue')

    def __str__(self):
        return '%s' % (self.name)

admin.site.register(Event)

class Area(models.Model):
    name = models.TextField(null=True, blank = True)
    description = models.TextField(null=True, blank = True)
    place_number = models.TextField(null=True, blank = True)
    event = models.ForeignKey('Event')

    def __str__(self):
        return '%s' % (self.name)

admin.site.register(Area)
