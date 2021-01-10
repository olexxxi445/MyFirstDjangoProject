from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from enjine.forms import ReqForm

from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def home(request):
	return render (request, 'enjine/index.html', {})

def about(request):
	return render(request, 'enjine/about.html')

def contact(request):
	return render(request, 'enjine/contact.html')
	
	
def buy(request):
	form = ReqForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('{}?sent=True'.format(reverse('buy')))

	return render(request, 'enjine/buy.html', {

		#'buy': buy,
		'form': form,
		'sent': request.GET.get('sent', False)
		})



