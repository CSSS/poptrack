from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count, Min, Sum, Avg

from poptrack.models import Filling, Stocking, Pop, Column

class IndexView(generic.ListView):
	template_name = 'index.html'

	def get(self, request, *args, **kwargs):
		return super(IndexView, self).get(request, *args, **kwargs)

	def get_queryset(self):
		return Filling.objects.all()

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		return context

class FillingForm(ModelForm):
	class Meta:
		model = Filling
		fields = ['pop', 'column', 'amount', 'was_empty']

@login_required()
def AddFilling(request):
	if (request.method == 'POST'):
		form = FillingForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.save()
			return HttpResponseRedirect(reverse('index'))
	else:
		form = FillingForm()
	return render(request, 'add.html', {'form': form})

def ViewStock(request):
	elem  = Pop.objects.annotate(stock = Sum('stocking__amount'))
	elem2 = Pop.objects.annotate(sold = Sum('filling__amount'))
	for i in range(len(elem)):
		elem[i].stock = elem[i].stock - elem2[i].sold
	return render(request, 'stock.html', {'stock': elem})
