from django.shortcuts import render
# to show the time we need to import datetime module
import datetime
# to get the time zone we need to import this also
from django.utils import timezone

# this show fuction tells us the actual time
def show(request):

	now = timezone.now()
	context = {
	'now' : now
	}
	return render(request, 'base.html', context)



