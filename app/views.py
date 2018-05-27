from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template


from app.forms import ContactForm


def index(request):
	return render(request, 'app/index.html')

def other(request):
    return render(request, 'app/other.html')

def about_us(request):
    return render(request, 'app/about_us.html')

def what_we_do(request):
    return render(request, 'app/what_we_do.html')

def service_pricing(request):
    return render(request, 'app/service_pricing.html')

def contact_sent(request, context):
	return render(request, 'app/contact_sent.html', context)

def contact(request):
	form_class = ContactForm

	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():

			contact_name = request.POST.get(
				'contact_name', '')

			contact_email = request.POST.get(
				'contact_email', '')
			form_content = request.POST.get('content', '')

			template = get_template('app/contact_template.txt')

			context = {
				'contact_name': contact_name, 
				'contact_email': contact_email, 
				'form_content': form_content,
			}
			content = template.render(context)

			email = EmailMessage(
				'New Contact Form Submission', 
				content, 
				'Your website ',
				['mclaughlin.john.duffy@gmail.com'], 
				headers = {'Reply-To': contact_email}
			)
			email.send()

			# send_mail('new mail', context['form_content'], 'jduffymclaughlin@gmail.com',
			# 	['mclaughlin.john.duffy@gmail.com'], 
			# 	fail_silently=False)

			#return render(request, 'app/contact_sent.html')
			return contact_sent(request, context)

	return render(request, 'app/contact.html', {'form': form_class})

