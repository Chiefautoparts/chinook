from django.shortcuts import render
from .models import River

# Create your views here.
def index(request):
	return render(request, 'rivers.html')

def displayRivers(request):
	rivers = River.objects.all()