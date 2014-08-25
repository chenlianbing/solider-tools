from django.contrib import admin
from wages.models import Wage

# Register your models here.
# admin.site.register(Wage)
'''
class WageAdmin2(admin.ModelAdmin):
	fields = ['housing_allowances', 'attence_bonus', 'performance', 'per34w', 'per31w', 'per28w', 'per24w', 'per20w', 'per16w', 'per11w', 'per6w', 'per0w', 'basic_wage', 'month']

admin.site.register(Wage, WageAdmin2)
'''

class WageAdmin2(admin.ModelAdmin):
	fieldsets = [
		(None,                     {'fields':['month']}),
		(None,                     {'fields':['basic_wage']}),
		('Commission coefficient', {'fields':['per0w', 'per6w', 'per11w', 'per16w', 'per20w', 'per24w', 'per28w', 'per31w', 'per34w' ]}),
		(None,                     {'fields':['performance']}),
		(None,                     {'fields':['attence_bonus']}),
		(None,                     {'fields':['housing_allowances']}),
	]
	
	list_display = ('month', 'basic_wage', 'per0w', 'per6w', 'per11w')
	list_filter = ['basic_wage', 'per6w']
	search_fields = ['basic_wage']
	
admin.site.register(Wage, WageAdmin2)
