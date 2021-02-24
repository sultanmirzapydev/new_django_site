

from django.shortcuts import render
# to show the time we need to import datetime module
import datetime
# to get the time zone we need to import this also
from django.utils import timezone
from .models import Blog
#from weather.views import weather
import requests
import json

# this show fuction tells us the actual time
def show(request):

	now = timezone.now()
	return now

def day_in_string(request):
	now = now = datetime.datetime.now()
	return now.strftime("%A")

def blogs(request):
	blogs = Blog.objects.order_by('-date').filter(is_published=True)
	return blogs

def base(request):
	now = show(request)
	str_day = day_in_string(request)
	blog_list = blogs(request)
	
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=e7e98c2c6ffd99bc079c09341ce82efd'
	city = 'hyderabad'

	response = requests.get(url.format(city)).json()
	
	city_weather = {
        'city':city,
        'temperature':response['main']['temp'],
        'description':response['weather'][0]['description'],
        'icon':       response['weather'][0]['icon'],

    }

   


	context = {
		'blogs':blog_list,
		'now':now,
		'day_in_string':str_day,
		'weather':city_weather,
	}

	return render(request, 'base.html', context)


