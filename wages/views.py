from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from wages.models import Wage

def calculator(request):
	latest_records = Wage.objects.order_by('month')[0]
	context = {'latest_wage_info': latest_records}
	
	return render(request, 'wages/panel.html', context)
	
def image_show(request, image_name):
	context = {'image_name':image_name}
	return render(request, 'wages/image.html', context)
	
'''	
latest_record.month + latest_record.basic_wage + latest_record.per0w + latest_record.per6w + latest_record.per11w
latest_record.per16w
latest_record.per20w
latest_record.per24w
latest_record.per28w
latest_record.per31w
latest_record.per34w
latest_record.performance
latest_record.attence_bonus
latest_record.housing_allowances
'''