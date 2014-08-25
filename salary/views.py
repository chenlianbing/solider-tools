from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic

from salary.models import Poll, Choices

class IndexView(generic.ListView):
	template_name = 'salary/index.html'
	context_object_name = 'latest_poll_list'
	
	def get_queryset(self):
		return Poll.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Poll
	template_name = 'salary/detail.html'

class ResultsView(generic.DetailView):
	model = Poll
	template_name = 'salary/results.html'
	
''' use generic view
def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	template = loader.get_template("salary/index.html")
	context = RequestContext(request, {'latest_poll_list':latest_poll_list,})
	
	#output = ', '.join([p.question for p in latest_poll_list])
	return HttpResponse(template.render(context))

def detail(request, poll_id):
	try:
		poll = Poll.objects.get(pk=poll_id)
	except Poll.DoesNotExist:
		raise Http404
	#return HttpResponse("You're looking at poll %s." %poll_id)
	return render(request, 'salary/detail.html', {'poll':poll})
	
def results(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'salary/results.html', {'poll':poll})
	#return HttpResponse("You're looking at the results of poll %s." %poll_id)
'''
def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choices_set.get(pk=request.POST['choice'])
	except (KeyError, Choices.DoesNotExist):
		return render(request, 'salary/detail.html', {
			'poll':p,
			'error_message': "You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('salary:results', args=(p.id, )))

# Create your views here.
