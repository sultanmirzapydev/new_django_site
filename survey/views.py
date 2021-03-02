from django.shortcuts import render, redirect
from .models import Choice, Feedback
from django.contrib import messages



def survey(request):
	if request.method == 'POST':
		
		user_id         = request.POST['user_id']
		user_name       = request.POST['user_name']
		first_question  = request.POST['item1_question']
		first_answer    = request.POST['1']
		second_question = request.POST['item2_question']
		second_answer   = request.POST['2']
		feedback_text   = request.POST['feedback']

		if request.user.is_authenticated:
			has_submitted = Feedback.objects.all().filter( user_id=user_id)
			if has_submitted:
				messages.error(request, 'you have already submitted, thank you ')

			#else:
			#	feedback = Feedback.objects.create(user_id=user_id, user_name=user_name, first_question=first_question,
			#	first_answer=first_answer, second_question=second_question, second_answer=second_answer,
			#	feedback_text=feedback_text)

			#	feedback.save()

			#	messages.success(request,'Thank you')

		else:
			feedback = Feedback.objects.create(user_id=user_id, user_name=user_name, first_question=first_question,
				first_answer=first_answer, second_question=second_question, second_answer=second_answer,
				feedback_text=feedback_text)
			feedback.save()

			messages.success(request,'Thank you')

		query = Choice.objects.all()
		return query
		

	else:
		query = Choice.objects.all()
		return query

	
	