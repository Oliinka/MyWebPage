from django.shortcuts import render

##pridano pro app contact
from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.contrib import messages


def index(request):
    return render(request, 'main/index.html')

def bio(request):
    return render(request, 'main/bio.html')

def code(request):
    return render(request, 'main/code.html')

def build(request):
    return render(request, 'main/build.html')
    
def live(request):
    return render(request, 'main/live.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
            return redirect('contact')  # Redirect back to the contact page
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})