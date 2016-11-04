from django.db import models
from django.utils.encoding import python_2_unicode_compatible

#@python_2_unicode_compatible  # only if you need to support Python 2
class FillUp(models.Model):
    odometer    = models.DecimalField(max_digits=8, decimal_places=2)
    gallons     = models.DecimalField(max_digits=6, decimal_places=3)
    cpg         = models.DecimalField(max_digits=5, decimal_places=3)
    fuel_type   = models.CharField(max_length=200)

