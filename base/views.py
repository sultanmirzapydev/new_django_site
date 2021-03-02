

from django.shortcuts import render
# to show the time we need to import datetime module
import datetime
# to get the time zone we need to import this also
from django.utils import timezone

from blog.models import Blog

from survey.views import survey
from weather.views import weather
import requests
import json
# this show fuction tells us the actual time
def show(request):

	now = timezone.now()
	return now


def day_in_string(request):
	now = now = datetime.datetime.now()
	return now.strftime("%A")


def blog_listview(request):
	blogs = Blog.objects.order_by('-date').filter(is_published=True)
	print(blogs)
	return blogs

	

def base(request):
	now = show(request)
	str_day = day_in_string(request)
	blog_list = blog_listview(request)
	query = survey(request)
	city_weather = weather(request)

   


	context = {
		'blogs':blog_list,
		'now':now,
		'day_in_string':str_day,
		'weather':city_weather,
		'query':query,
	}

	return render(request, 'base.html', context)


