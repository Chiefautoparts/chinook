from django.shortcuts import render
from django.views import generic
from .models import River

# Create your views here.
class RiverListView(generic.DetailView):
	model = River 
	def river_detail_view(request, primary_key):
		try:
			river = River.objects.get(pl=primary_key)
		except River.DoesNotExist:
			raise Http404('No Such River')

		return render(request, 'river/river_detail.html', context={'river': river})

def index(request):
	return render(request, 'rivers.html')

def displayRivers(request):
	rivers = River.objects.all()
	context  = {
		'rivers': rivers,
	}

	return render(request, 'trips/river_details.html', context=context)