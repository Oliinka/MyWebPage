from django.shortcuts import render, redirect

from .forms import ContactForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
##email form
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send email
            email_body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\nMessage:\n{message}"
            email_subject = f"Contact Form Submission: {subject}"
            sender_email = 'olga.titzenthaler@gmail.com'  # Update with your email
            recipient_email = 'olga.titzenthaler@gmail.com'  # Update with your admin email

            # Send email using Django's EmailMessage
            email = EmailMessage(
                email_subject,
                email_body,
                sender_email,
                [recipient_email],
                reply_to=[email],
            )
            email.send()

            return redirect('success')  # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

##sucessfuly sent mail form
def success(request):
    return render(request, 'contact/success.html')

