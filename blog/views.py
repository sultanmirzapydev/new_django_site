from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_detailsview(request, pk):
	instance = get_object_or_404(Blog, pk=pk)


	
	

	context = {
		'instance':instance
	}

	return render(request, 'blogs/blog.html', context)