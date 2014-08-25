from django.db import models
from datetime import date

# Create your models here.
class Wage(models.Model):
	month = models.DateField('Crate Date')
	basic_wage = models.PositiveIntegerField(default = 1000)
	per0w = models.DecimalField(max_digits=5, decimal_places=4, default=0.0100)
	per6w = models.DecimalField(max_digits=5, decimal_places=4, default=0.0125)
	per11w = models.DecimalField(max_digits=5, decimal_places=4, default=0.0150)
	per16w = models.DecimalField(max_digits=5, decimal_places=4, default=0.0175)
	per20w = models.DecimalField(max_digits=5, decimal_places=4, default=0.0200)
	per24w = models.DecimalField(max_digits=5, decimal_places=4, default=0.0225)
	per28w = models.DecimalField(max_digits=5, decimal_places=4, default=0.0250)
	per31w = models.DecimalField(max_digits=5, decimal_places=4, default=0.0275)
	per34w = models.DecimalField(max_digits=5, decimal_places=4, default=0.0300)
	performance = models.PositiveIntegerField(default = 800)
	attence_bonus = models.PositiveIntegerField(default = 200)
	housing_allowances = models.PositiveIntegerField(default = 100)
	
	def __str__(self):
		return str(self.month) + ": " + "basic_wage:"+ str(self.basic_wage) + ", self.per0w:" + str(self.per0w) 
		