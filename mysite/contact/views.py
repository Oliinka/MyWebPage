from django.shortcuts import render

# Create your views here.
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Add any additional logic (e.g., sending emails) here
            return redirect('contact_success')  # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})