from . import views
from django.urls import path

urlpatterns = [
	path('rivers/', views.RiverListView.as_view(), name='rivers'),
	path('river/<int:ok>', views.RiverListView.as_view(), name='river-detail'),
]