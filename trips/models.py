from django.db import models

# Create your models here.
class River(models.Model):
	name = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	itinerary = models.TextField(max_length=1000)
	duration = models.CharField(max_length=100)
	difficulty = models.IntegerField()

	class Meta:
		ordering = ['difficulty']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('river', args=[str(self.id)])