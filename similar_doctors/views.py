from django.shortcuts import render

from operator import itemgetter

from .models import Doctor, DOCTOR_TYPES, Rating

def index(request):
	doctors_query = Doctor.objects.all()
	doctors = {}
	for doctor in doctors_query:
		# types = give_type_strings(doctor.type)
		doctors[doctor.id] = makeJSONdoctor(doctor, True)
	context={'doctors': doctors}
	print(context)
	return render(request, 'similar_doctors/index.html', context)
	
def doctor_info(request, doctor_id):
	doctor_query = Doctor.objects.filter(id=doctor_id)
	similar = doctors_like_this(doctor_query[0].name, doctor_query[0].location, doctor_query[0].type)
	context = makeJSONdoctor(doctor_query[0])
	context['similar'] = similar
	return render(request, 'similar_doctors/doctor_info.html', context)
	
def give_type_strings(type):
	return [type.choices.get(int(i)) if i.isdigit() else type.choices.get(i) for i in type]

def doctors_like_this(name, location, types):
	similar = {}
	max = 0
	l = "".join(location.split(" ")).lower()
	doctors = Doctor.objects.all()
	for type in types:
		for doctor in doctors:
			if doctor.name == name:
				continue
			elif type in doctor.type:
				if doctor.name not in similar.keys():
					similar[doctor.name] = makeJSONdoctor(doctor)
					similar[doctor.name]['score'] = 1
					dl = "".join(doctor.location.split(" ")).lower()
					if l == dl:
						similar[doctor.name]['score'] += 1
				else:
					similar[doctor.name]['score'] += 1
					if similar[doctor.name]['score'] > max:
						max = similar[doctor.name]['score']
	return similar
	
def doctor_rating_avg(doctor):
	ratings = Rating.objects.filter(doctor=doctor)
	if len(ratings) == 0:
		return 0
	sum = 0
	for rating in ratings:
		sum += int(rating.rating)
	return sum/len(ratings)
	
def makeJSONdoctor(doctor, s=False):
	if not s:
		return {
			'id':doctor.id,
			'name':doctor.name,
			'location':doctor.location,
			'description':doctor.description,
			'type':doctor.type,
			'rating':doctor_rating_avg(doctor)
		}
	else:
		return {
			'id':doctor.id,
			'name':doctor.name,
			'location':doctor.location,
			'description':doctor.description,
			'type':give_type_strings(doctor.type),
			'rating':doctor_rating_avg(doctor)
		}