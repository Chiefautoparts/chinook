from . import views
from django.urls import path

app_name='trips'

urlpatterns = [
	path('', views.displayRivers, name='rivers'),
	path('river/<int:ok>', views.RiverListView.as_view(), name='river-detail'),
]