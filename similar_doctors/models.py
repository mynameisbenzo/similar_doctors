from django.db import models
from multiselectfield import MultiSelectField

DOCTOR_TYPES = (
	('HEART', 'CARDIOLOGIST'),
	('GENERAL', 'GENERAL'),
	('BRAIN', 'NEUROLOGIST'),
	('EYE', 'OPTHALMOLOGIST'),
	('EYE', 'OPTOMETRIST'),
	('SKIN', 'DERMATOLOGIST'),
	('MENTAL', 'PSYCHOLOGIST'),
	('MENTAL', 'PSYCHIATRIST'),
	('TEETH', 'DENTIST'),
	('TEETH', 'ORTHODONIST'),
	('COSMETIC', 'PLASTIC SURGEON'),
)

# Create your models here.
class Doctor(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	type = MultiSelectField(choices=DOCTOR_TYPES)
	description = models.CharField(max_length=500, default="A great doctor.")
	
	class Meta:
		verbose_name_plural = 'doctors'
		
	def __str__(self):
		return self.name
		
class Rating(models.Model):
	ratings = [(str(i), str(i)) for i in range(1,6)]
	rating = models.CharField(max_length=2, choices=ratings)
	doctor = models.ForeignKey(
		Doctor,
		on_delete=models.CASCADE
	)
	
	class Meta:
		verbose_name_plural = 'ratings'
		
	def __str__(self):
		return self.rating + " " + self.doctor.name